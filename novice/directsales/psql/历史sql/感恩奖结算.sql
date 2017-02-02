-- Function: public.awards_thanksgiving(integer, numeric)

-- DROP FUNCTION public.awards_thanksgiving(integer, numeric);

CREATE OR REPLACE FUNCTION public.awards_thanksgiving(
    IN awards_nodeid integer,
    IN awards_pricein numeric)
  RETURNS TABLE(memberlevel character varying, type character varying, price numeric, io character varying, overage numeric, pay_by character varying, remark text, track_id integer, joined timestamp with time zone) AS
$BODY$
DECLARE
    child_id integer[];
    chile_priority integer[];
    nodeid integer;
    sum_priority integer;
    one_priority integer;
    x integer;
    each_price numeric;
    memberlevelid integer;
BEGIN
    --寻找awards_nodeid节点的所有直推节点
    select ARRAY_AGG(id),array_agg(priority) into child_id,chile_priority from public.directsales_doubletrack where directpushuser_id = awards_nodeid;
    --求出总份数
    sum_priority := 0;
    FOREACH x IN ARRAY chile_priority
    LOOP
       sum_priority := sum_priority + x;
    END LOOP;
    --每一份可分配的金额
    each_price := (awards_pricein * 0.1) / sum_priority;
    --开始分配奖金
    FOREACH nodeid IN ARRAY child_id
    LOOP
        --获取该节点会员信息
        select dm.id,dm.name into memberlevelid,memberlevel
            from public.directsales_doubletrack as dd INNER JOIN public.directsales_memberlevel as dm 
            on dd.identity_id=dm.id
            where dd.id=nodeid;
        --获取该节点的权重
        select priority into one_priority from public.directsales_doubletrack where id = nodeid;
        ----@开始计算感恩奖
        price := each_price * one_priority;
        ----@获取其他信息
        ------查询当前现金余额，层奖系统发放给现金币账户,此次奖金未发放时
        select cash into overage from public.directsales_bonus as db where db.track_id=nodeid;
        type := 'thanksgiving_awards';
        io := 'I';
        pay_by := 'system';
        remark := '感恩奖奖金';
        track_id := nodeid;
        joined := now();
        return NEXT;
    END LOOP;
    RETURN;
END
$BODY$
  LANGUAGE plpgsql;

