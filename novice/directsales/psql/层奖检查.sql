select * from awards_layer(5,1000,true)


SELECT string_to_array(path,'/'), depth 
FROM directsales_doubletrack WHERE id = 5;


select count(node_id) into layer_count from public.directsales_nodehistory where node_id=nodeid::integer and depth=track_depth;


--select id,parent_id,path,depth from directsales_doubletrack
INSERT INTO "directsales_doubletrack" 
("user_id", "parent_id", "isright", "identity_id", "directpushuser_id", "name", "phone", 
"address", "bank", "bank_account", "pay_password", "depth", "path", 
"priority", "directpush_path", "joined", "updated") 
VALUES (5, 1, true, 1, 1, 'test4', '13655917317', '海南省海口市美兰区', '2', '767868768768712312312312', '123456', 
NULL, NULL, NULL, NULL, '2017-01-30T04:26:55.747617+00:00'::timestamptz, 
'2017-01-30T04:26:55.747653+00:00'::timestamptz) 
RETURNING "directsales_doubletrack"."id";



