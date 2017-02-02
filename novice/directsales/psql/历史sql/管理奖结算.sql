-- Function: public.awards_manage(integer, boolean)

-- DROP FUNCTION public.awards_manage(integer, boolean);

CREATE OR REPLACE FUNCTION public.awards_manage(
    IN meetnode_id integer,
    IN meet_pricein numeric)
  RETURNS TABLE(memberlevel character varying, type character varying, price numeric, io character varying, overage numeric, pay_by character varying, remark text, track_id integer, joined timestamp with time zone) AS
$BODY$
DECLARE
    parent_id character varying[];
    nodeid character varying;
    node_seniority_num integer;
    memberlevelid integer;
    memberlevel character varying;
    f_percentage numeric;
    f_seniority_num integer;
BEGIN
    --寻找meetnode_id节点的所有父带节点
    SELECT string_to_array(directpush_path,'/') INTO parent_id FROM public.directsales_doubletrack WHERE id = meetnode_id;
    --去头尾
    parent_id := array_remove(parent_id,'');
    parent_id := array_remove(parent_id,meetnode_id::character varying);

    FOREACH nodeid IN ARRAY parent_id
    LOOP
        --判断此节点是否可以结算管理奖
        ----@1.得到nodeid与directpushuserid之间的path,并计算代数
        select get_txt_count(substr(directpush_path,strpos(directpush_path,nodeid::character varying),strpos(directpush_path,meetnode_id::character varying)-strpos(directpush_path,nodeid::character varying)),'/')
        into node_seniority_num
        from directsales_doubletrack
        where directpush_path like '%' || nodeid::character varying || '%' || meetnode_id::character varying;
        ----@2.获取该节点会员信息
        select dm.id,dm.name into memberlevelid,memberlevel
            from public.directsales_doubletrack as dd INNER JOIN public.directsales_memberlevel as dm 
            on dd.identity_id=dm.id
            where dd.id=nodeid::integer;
        ----@3.获取该会员相关等级的可计算代数及计算比例
        select percentage,seniority_num into f_percentage,f_seniority_num from public.directsales_awards where memberlevel_id=memberlevelid and keyword='manage';
        ----@4.判断代数是否超过限制
        IF node_seniority_num > f_seniority_num THEN
            CONTINUE;
        END IF;
        ----@5.如无超过，开始计算管理奖
        price := meet_pricein * f_percentage;
        ----@6.获取其他信息
        ------查询当前现金余额，层奖系统发放给现金币账户,此次奖金未发放时
        select cash into overage from public.directsales_bonus as db where db.track_id=nodeid::integer;
        type := 'manage_awards';
        io := 'I';
        pay_by := 'system';
        remark := '管理奖奖金';
        track_id := nodeid::integer;
        joined := now();
        return NEXT;
    END LOOP;
    RETURN;
END
$BODY$
  LANGUAGE plpgsql;
