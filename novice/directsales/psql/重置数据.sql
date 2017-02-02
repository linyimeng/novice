truncate table directsales_transactionhistory CASCADE;
truncate table directsales_nodehistory;
truncate table directsales_withdrawhistory;


select setval('directsales_bonus_id_seq', 1, false);
select setval('directsales_doubletrack_id_seq',1,false);
select setval('directsales_nodehistory_id_seq',1,false);
select setval('directsales_transactionhistory_id_seq',1,false);

delete from directsales_bonus;
select setval('directsales_bonus_id_seq',2,false);
delete from directsales_doubletrack where id<>1;
select setval('directsales_doubletrack_id_seq',2,false);
delete from auth_user where id<>1;
select setval('auth_user_id_seq',2,false);