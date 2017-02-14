-- Function: public.awards_seepoint(integer, numeric)

-- DROP FUNCTION public.awards_seepoint(integer, numeric);

CREATE OR REPLACE FUNCTION public.awards_seepoint(
    IN trackid integer,
    IN pricein numeric)
  RETURNS TABLE(source_track integer, memberlevel character varying, type character varying, price numeric, io character varying, overage numeric, pay_by character varying, remark text, track_id integer, joined timestamp with time zone) AS
$BODY$
DECLARE
    parent_id character varying[];
    nodeid character varying;
    node_layer_num integer;
    memberlevelid integer;
    f_percentage numeric;
    f_layer_num integer;
    awards numeric;
    thanksgiving_count integer;
    true_count integer;
    false_count integer;
    postion boolean;
BEGIN
    --寻找trackid节点的所有父代节点
    SELECT string_to_array(path,'/') INTO parent_id FROM public.directsales_doubletrack WHERE id = trackid;
    if parent_id is null then
        return;
    end if;
    --去头尾
    parent_id := array_remove(parent_id,'');
    parent_id := array_remove(parent_id,trackid::character varying);

    FOREACH nodeid IN ARRAY parent_id
    LOOP
        --判断此节点是否可以结算见点奖
        ----@1.得到nodeid与parent之间的path,并计算层数
        select get_txt_count(substr(path,strpos(path,nodeid::character varying),strpos(path,trackid::character varying)-strpos(path,nodeid::character varying)),'/')
        into node_layer_num
        from directsales_doubletrack
        where path like '%' || nodeid::character varying || '%' || trackid::character varying;
        ----@2.获取该节点会员信息
        select dm.id,dm.name into memberlevelid,memberlevel
            from public.directsales_doubletrack as dd INNER JOIN public.directsales_memberlevel as dm 
            on dd.identity_id=dm.id
            where dd.id=nodeid::integer;
        ----@3.获取该会员相关等级的可计算层数及计算比例
        select percentage,layer_num,name into f_percentage,f_layer_num,remark from public.directsales_awards where memberlevel_id=memberlevelid and keyword='seepoint';
        ----@4.判断代数是否超过限制
        IF node_layer_num > f_layer_num THEN
            CONTINUE;
        END IF;
        ----@5.如无超过，判断大小区
        -------@1.判断track在node节点的左或右
        select is_right(nodeid::integer,trackid) into postion;
        -------@2.计算左右两区大小
        select get_node_child_count_recursion(nodeid::integer,true) into true_count;
        select get_node_child_count_recursion(nodeid::integer,false) into false_count;
        
        IF true_count > false_count THEN
            if postion <> true then
                CONTINUE;
            end if;
        ELSIF true_count < false_count THEN
            if postion <> false then
                CONTINUE;
            end if;
        END IF;
        ----@5.如无超过，开始计算见点奖
        awards := pricein * f_percentage;
        select priceout,directpush_count into price,thanksgiving_count from get_price(awards,nodeid::integer);
        IF thanksgiving_count<>0 THEN
            return query select * from awards_thanksgiving(nodeid::integer,awards);
        END IF;
        ----@6.获取其他信息
        overage := 0;
        type := 'gold';
        io := 'I';
        pay_by := 'system';
        track_id := nodeid::integer;
        joined := now();
        source_track := trackid;
        return query select * from awards_fee(nodeid::integer,awards);
        return NEXT;
    END LOOP;
    RETURN;
END
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.awards_seepoint(integer, numeric)
  OWNER TO ym;
