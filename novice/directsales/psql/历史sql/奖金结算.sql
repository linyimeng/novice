-- Function: public.awards(integer, numeric, boolean)

-- DROP FUNCTION public.awards(integer, numeric, boolean);

CREATE OR REPLACE FUNCTION public.awards(
    IN trackid integer,
    IN pricein numeric,
    IN debug boolean)
  RETURNS TABLE(memberlevel character varying, type character varying, price numeric, io character varying, overage numeric, pay_by character varying, remark text, track_id integer, joined timestamp with time zone) AS
$BODY$
DECLARE

BEGIN
    debug := true;
    return query select * from awards_directpush(trackid,pricein)
                 union
                 select * from awards_seepoint(trackid,pricein)
                 union
                 select * from awards_layer(trackid, pricein, debug)
                 union
                 select * from awards_meet(trackid, pricein, debug);
END
$BODY$
  LANGUAGE plpgsql;
