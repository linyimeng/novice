-- Function: public.awards_directpush(integer, numeric)
-- DROP FUNCTION public.awards_directpush(integer, numeric);
--层奖计算,当出现节点时实时计算，trackid为出现节点的id
CREATE OR REPLACE FUNCTION public.awards_layer(
    IN trackid integer,
    IN pricein numeric,
    IN is_debug boolean)
  RETURNS TABLE(memberlevel character varying, type character varying, price numeric, io character varying, overage numeric, 
                pay_by character varying, remark text, track_id integer, joined timestamp with time zone) AS
$BODY$
DECLARE
    parent_id character varying[];
    track_depth integer;
    nodeid character varying;
    layer_count integer;
    f_follow_id integer;
    f_right Boolean;
    samelayer_count integer;
    memberlevelid integer;
    f_percentage numeric;
    result record;
BEGIN
    --寻找该节点的所有父节点
    SELECT string_to_array(path,'/'), depth INTO parent_id,track_depth FROM directsales_doubletrack WHERE id = trackid;
    --去头尾
    parent_id := array_remove(parent_id,'');
    parent_id := array_remove(parent_id,trackid::character varying);

    FOREACH nodeid IN ARRAY parent_id
    LOOP
        --判断此节点该层层奖是否发生过
        select count(node_id) into layer_count from public.directsales_nodehistory where node_id=nodeid::integer and depth=track_depth;
        IF layer_count <> 0 THEN
            CONTINUE;
        END IF;
        --如无发生过，开始判断是否存在层奖
        ----@1.判断左右
        select not is_right into f_right from is_right(nodeid::integer, trackid);
        ----@2.获取父节点下对应方向相同的深度的节点,如出现节点在此父节点右边，则获取一个父节点左边相同深度的节点,如存在节点，则继续，如几点个数为0,判断下一个节点
        select count(*),samelayer.trackid into samelayer_count,f_follow_id from find_samelayer_node(nodeid::integer,f_right,track_depth) as samelayer group by samelayer.trackid limit 1;
        IF samelayer_count is null or samelayer_count = 0 THEN
            CONTINUE;
        END IF;
        --确定层奖产生,并计算生成相关交易记录
        ----@1获取该节点会员信息
        select dm.id,dm.name into memberlevelid,memberlevel
            from public.directsales_doubletrack as dd INNER JOIN public.directsales_memberlevel as dm 
            on dd.identity_id=dm.id
            where dd.id=nodeid::integer;
        ----@2获取层奖提成比例,并计算奖金
        select percentage into f_percentage from public.directsales_awards where memberlevel_id=memberlevelid and keyword='layer';
        price := pricein * f_percentage;
        ----@3查询当前现金余额，层奖系统发放给现金币账户,此次奖金未发放时
        select cash into overage from public.directsales_bonus as db where db.track_id=nodeid::integer;
        ----@4其他记录信息
        type := 'layer_awards';
        io := 'I';
        pay_by := 'system';
        remark := '层奖奖金';
        track_id := nodeid::integer;
        joined := now();
        ----@记录层奖计算记录
        IF NOT is_debug THEN
            insert into public.directsales_nodehistory(node_id,follow_id,depth,type,joined,awards) 
                                          values(nodeid::integer,f_follow_id,track_depth,'layer',now(),price);
        END IF;
        return NEXT;
    END LOOP;
    RETURN;
END
$BODY$
  LANGUAGE plpgsql;

--SELECT * FROM directsales_awardshistory
--select * from directsales_transactionhistory
--SELECT * FROM awards_layer(8,1000,true)
SELECT NULL = 0::BOOLEAN



--寻找节点下相同层数的节点
CREATE OR REPLACE FUNCTION public.find_samelayer_node(nodeid integer, is_right Boolean, f_depth integer)
RETURNS TABLE(trackid integer) AS
$$
DECLARE
    parent_path character varying;
    parent_depth integer;
    child_depth integer;
    child_node_id integer;
    child_path character varying;
BEGIN
    --得到nodeid节点的路径
    select path,depth into parent_path, parent_depth from public.directsales_doubletrack where id=nodeid;
    child_depth := parent_depth + 1;
    --得到nodeid下的子节点，左或右
    select id into child_node_id from public.directsales_doubletrack where path like '%'||parent_path||'/%' and depth=child_depth and isright=is_right;
    --得到子节点的path信息
    select path into child_path from public.directsales_doubletrack where id=child_node_id;
    --得到子节点下的所有节点，即nodeid节点的所有is_right(左或右)节点，这边添加深度条件，求相同深度下，相同的节点
    RETURN query select id from public.directsales_doubletrack where path like '%'||child_path||'%' and depth = f_depth;
    RETURN;
END
$$
LANGUAGE plpgsql;

--给定一个父节点和子节点，判断子节点是在父节点的左边或者右边
CREATE OR REPLACE FUNCTION is_right(parentid integer,childid integer,out is_right Boolean)
RETURNS Boolean AS
$$
DECLARE
    parent_path character varying;
    parent_depth integer;
    child_depth integer;
    child_node_id integer;
    child_path character varying;
    node_count integer;
BEGIN
    --得到nodeid节点的路径
    select path,depth into parent_path, parent_depth from public.directsales_doubletrack where id=parentid;
    child_depth := parent_depth + 1;
    --得到nodeid下的子节点，从右节点开始
    select id into child_node_id from public.directsales_doubletrack where path like '%'||parent_path||'/%' and depth=child_depth and isright=true;
    --得到子节点的path信息
    select path into child_path from public.directsales_doubletrack where id=child_node_id;
    --判断左右
    select count(id) into node_count from public.directsales_doubletrack where path like '%'||child_path||'%' and id=childid;
    IF node_count > 0 THEN
        is_right := true;
    ELSE
        is_right := false;
    END IF;
    RETURN;
END
$$
LANGUAGE plpgsql;







