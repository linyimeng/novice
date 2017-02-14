update directsales_bonus as db set gold = sumprice
from (select (COALESCE((select sum(price) from directsales_transactionhistory as dti where dti.io='I' group by dti.track_id having dti.track_id=dt.track_id),0) -
       COALESCE((select sum(price) from directsales_transactionhistory as dto where dto.io='O' group by dto.track_id having dto.track_id=dt.track_id),0)) as sumprice,
       track_id
from directsales_transactionhistory as dt group by dt.track_id) as t1
where db.track_id = t1.track_id;





--select (COALESCE((select sum(price) from directsales_transactionhistory as dti where dti.io='I' group by dti.track_id having dti.track_id=dt.track_id),0) -
--      COALESCE((select sum(price) from directsales_transactionhistory as dto where dto.io='O' group by dto.track_id having dto.track_id=dt.track_id),0)) as sumprice,
--       track_id
--from directsales_transactionhistory as dt group by dt.track_id;