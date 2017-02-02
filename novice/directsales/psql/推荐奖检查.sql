select * from awards_directpush(5,1000)


select directpushuser_id
 from public.directsales_doubletrack where id = 5;

 select identity_id from public.directsales_doubletrack as dd where dd.id = 1;
select da.percentage from public.directsales_awards as da where da.memberlevel_id = 4 and da.keyword='directpush'