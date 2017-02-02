WITH RECURSIVE child
AS (
     --第一个查询作为递归的基点(锚点)
     SELECT id,user_id,identity_id,joined,updated,parent_id,directpushuser_id,isright
     FROM directsales_doubletrack 
     WHERE id=1
     UNION ALL
     --第二个查询作为递归成员,下属成员的结果为空时，此递归结束。
     SELECT dd.id,dd.user_id,dd.identity_id,dd.joined,dd.updated,dd.parent_id,dd.directpushuser_id,dd.isright
     FROM directsales_doubletrack AS dd 
     INNER JOIN child
     ON child.id = dd.parent_id
   )
SELECT id,user_id,identity_id,parent_id,directpushuser_id,
	(SELECT count(*) FROM child as ch WHERE ch.directpushuser_id=child.id) AS directpushcount,
	get_node_child_count(id,true) AS rightcount,
	get_node_child_count(id,false) AS leftcount
FROM child
WHERE id<>1
