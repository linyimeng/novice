--DROP FUNCTION awards_directpush(integer,numeric)

CREATE OR REPLACE FUNCTION public.awards_directpush(
    trackid integer,
    pricein numeric(10,2)
    )
    RETURNS TABLE(memberlevel character varying(30),type character varying(20),price numeric(10,2),io character varying(1),overage numeric(10,2),pay_by character varying(30),remark text,track_id integer,joined timestamp with time zone) AS
    
$$
Declare
    member_id integer;
    parent integer;
    memberlevel_name character varying(30);
    directpushuser_id integer;
    percentage numeric(10,2);
    awards numeric(10,2);
BEGIN
    --获取会员级别,及会员信息
    select identity_id,parent_id into member_id,parent from public.directsales_doubletrack as dd where dd.id = trackid;
    select name into memberlevel_name from public.directsales_memberlevel as dm where dm.id = member_id;
    --获取奖金比例
    select da.percentage into percentage from public.directsales_awards as da where da.memberlevel_id = member_id and da.keyword='directpush';
    --计算奖金
    awards := pricein*percentage;

    --生成相关记录
    memberlevel := memberlevel_name;
    type := 'directpush_awards';
    price := awards;
    io := 'I';
    select cash into overage from public.directsales_bonus as db where db.track_id=trackid;
    pay_by := 'system';
    remark := '推荐奖';
    track_id := parent;
    joined := now();
    return QUERY select memberlevel as memberlevel,type,price,io,overage,pay_by,remark,track_id,joined;
END
$$
  LANGUAGE plpgsql;

--select awards_directpush(1,30000)

--select * from awards_directpush(1,30000)

--select "Memberlevel" from directsales_transactionhistory
--insert into directsales_transactionhistory("Memberlevel",type,price,io,overage,pay_by,remark,joined,track_id) select awards_directpush(1,30000)

  