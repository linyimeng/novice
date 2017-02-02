-- Function: public.awards_seepoint(integer, numeric)

-- DROP FUNCTION public.awards_seepoint(integer, numeric);

CREATE OR REPLACE FUNCTION public.awards_seepoint(
    IN trackid integer,
    IN pricein numeric)
  RETURNS TABLE(memberlevel character varying, type character varying, price numeric, io character varying, overage numeric, pay_by character varying, remark text, track_id integer, joined timestamp with time zone) AS
$BODY$
DECLARE
    parent_id character varying[];
    nodeid character varying;
    node_layer_num integer;
    memberlevelid integer;
    memberlevel character varying;
    f_percentage numeric;
    f_layer_num integer;
BEGIN
    --寻找trackid节点的所有父代节点
    SELECT string_to_array(directpush_path,'/') INTO parent_id FROM public.directsales_doubletrack WHERE id = trackid;
    --去头尾
    parent_id := array_remove(parent_id,'');
    parent_id := array_remove(parent_id,trackid::character varying);

    FOREACH nodeid IN ARRAY parent_id
    LOOP
        --判断此节点是否可以结算见点奖
        ----@1.得到nodeid与directpushuserid之间的path,并计算代数
        select get_txt_count(substr(directpush_path,strpos(directpush_path,nodeid::character varying),strpos(directpush_path,trackid::character varying)-strpos(directpush_path,nodeid::character varying)),'/')
        into node_layer_num
        from directsales_doubletrack
        where directpush_path like '%' || nodeid::character varying || '%' || trackid::character varying;
        ----@2.获取该节点会员信息
        select dm.id,dm.name into memberlevelid,memberlevel
            from public.directsales_doubletrack as dd INNER JOIN public.directsales_memberlevel as dm 
            on dd.identity_id=dm.id
            where dd.id=nodeid::integer;
        ----@3.获取该会员相关等级的可计算代数及计算比例
        select percentage,layer_num into f_percentage,f_layer_num from public.directsales_awards where memberlevel_id=memberlevelid and keyword='seepoint';
        ----@4.判断代数是否超过限制
        IF node_layer_num > f_layer_num THEN
            CONTINUE;
        END IF;
        ----@5.如无超过，开始计算管理奖
        price := pricein * f_percentage;
        ----@6.获取其他信息
        ------查询当前现金余额，层奖系统发放给现金币账户,此次奖金未发放时
        select cash into overage from public.directsales_bonus as db where db.track_id=nodeid::integer;
        type := 'seepoint_awards';
        io := 'I';
        pay_by := 'system';
        remark := '见点奖奖金';
        track_id := nodeid::integer;
        joined := now();
        return NEXT;
    END LOOP;
    RETURN;
END
$BODY$
  LANGUAGE plpgsql;
