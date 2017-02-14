-- Function: public.awards_directpush(integer, numeric)

-- DROP FUNCTION public.awards_directpush(integer, numeric);

CREATE OR REPLACE FUNCTION public.awards_directpush(
    IN trackid integer,
    IN pricein numeric)
  RETURNS TABLE(source_track integer, memberlevel character varying, type character varying, price numeric, io character varying, overage numeric, pay_by character varying, remark text, track_id integer, joined timestamp with time zone) AS
$BODY$
Declare
    member_id integer;
    directpush_id integer;
    memberlevel_name character varying(30);
    percentage numeric(10,2);
    awards_name character varying(30);
    awards numeric(10,2);
    thanksgiving_count integer;
BEGIN
    --判断是否有推荐人
    select directpushuser_id into directpush_id from public.directsales_doubletrack where id = trackid;
    if directpush_id is null then
        return;
    end if;
    --获取推荐人会员级别,及推荐人会员信息
    select identity_id into member_id from public.directsales_doubletrack as dd where dd.id = directpush_id;
    select name into memberlevel_name from public.directsales_memberlevel as dm where dm.id = member_id;
    --获取奖金比例
    select da.percentage,name into percentage,awards_name from public.directsales_awards as da where da.memberlevel_id = member_id and da.keyword='directpush';
    --计算奖金
    awards := pricein*percentage;
    --生成相关记录
    memberlevel := memberlevel_name;
    type := 'gold';
    select priceout,directpush_count into price,thanksgiving_count from get_price(awards,trackid);
    io := 'I';
    overage := 0;
    pay_by := 'system';
    remark := awards_name;
    track_id := directpush_id;
    joined := now();
    source_track := trackid;
    --计算感恩奖
    --if thanksgiving_count = 0 then
    --   return next;
    --else
    --    return QUERY select memberlevel as memberlevel,type,price,io,overage,pay_by,remark,track_id,joined union select * from awards_thanksgiving(trackid, pricein);
    --end if;
    return next;
    return query select * from awards_fee(directpush_id,awards);
END
$BODY$
  LANGUAGE plpgsql VOLATILE
  COST 100
  ROWS 1000;
ALTER FUNCTION public.awards_directpush(integer, numeric)
  OWNER TO ym;
COMMENT ON FUNCTION public.awards_directpush(integer, numeric) IS '推荐奖计算';
