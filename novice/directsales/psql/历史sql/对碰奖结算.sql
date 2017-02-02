-- Function: public.awards_meet(integer, numeric, boolean)

-- DROP FUNCTION public.awards_meet(integer, numeric, boolean);

CREATE OR REPLACE FUNCTION public.awards_meet(
    IN trackid integer,
    pricein numeric,
    IN is_debug boolean)
  RETURNS TABLE(memberlevel character varying, type character varying, price numeric, io character varying, overage numeric, pay_by character varying, remark text, track_id integer, joined timestamp with time zone) AS
$BODY$
DECLARE
    parent_id character varying[];
    track_depth integer;
    nodeid integer;
    node_count integer;
    f_right Boolean;
    f_follow_id integer;
    memberlevelid integer;
    f_percentage numeric;
BEGIN
    --寻找该节点的所有父节点
    SELECT string_to_array(path,'/'), depth INTO parent_id,track_depth FROM directsales_doubletrack WHERE id = trackid;
    --去头尾
    parent_id := array_remove(parent_id,'');
    parent_id := array_remove(parent_id,trackid::character varying);

    FOREACH nodeid IN ARRAY parent_id
    LOOP
        --判断此节点是否参与过层奖，对碰奖
        select count(*) into node_count from public.directsales_nodehistory where node_id=nodeid::integer or follow_id=nodeid::integer;
        IF node_count <> 0 THEN
            CONTINUE;
        END IF;
        --如无发生过，开始判断是否存在对碰奖
        ----@1.判断左右
        select not is_right into f_right from is_right(nodeid::integer, trackid);
        ----@2.获取父节点下对应方向存在的可结算节点，并返回节点id
        select meet.trackid into f_follow_id from find_meet_node(nodeid::integer,f_right) as meet group by meet.trackid limit 1;
        IF f_follow_id is null THEN
            CONTINUE;
        END IF;
        --确定对碰奖产生,并计算生成相关交易记录
        ----@1获取该节点会员信息
        select dm.id,dm.name into memberlevelid,memberlevel
            from public.directsales_doubletrack as dd INNER JOIN public.directsales_memberlevel as dm 
            on dd.identity_id=dm.id
            where dd.id=nodeid::integer;
        --@2获取对碰奖提成比例,并计算奖金
        --select percentage into f_percentage from public.directsales_awards where memberlevel_id=memberlevelid and keyword='layer';
        select 0.12 into f_percentage;
        price := pricein * f_percentage;
        ----@3查询当前现金余额，层奖系统发放给现金币账户,此次奖金未发放时
        select cash into overage from public.directsales_bonus as db where db.track_id=nodeid::integer;
        ----@4其他记录信息
        type := 'meet_awards';
        io := 'I';
        pay_by := 'system';
        remark := '对碰奖奖金';
        track_id := nodeid::integer;
        joined := now();
        ----@记录对碰奖计算记录
        IF NOT is_debug THEN
            insert into public.directsales_nodehistory(node_id,follow_id,depth,type,joined,awards) 
                                          values(trackid,f_follow_id,track_depth,'meet',now(),price);
        END IF;
        return NEXT;
        return query select * from awards_manage(nodeid,price);
    END LOOP;
    RETURN;
END
$BODY$
  LANGUAGE plpgsql;
