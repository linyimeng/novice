-- Function: public.find_meet_node(integer, boolean, integer)

-- DROP FUNCTION public.find_meet_node(integer, boolean, integer);

CREATE OR REPLACE FUNCTION public.find_meet_node(
    IN nodeid integer,
    IN is_right boolean)
  RETURNS TABLE(trackid integer) AS
$BODY$DECLARE
    parent_path character varying;
    parent_depth integer;
    child_depth integer;
    child_node_id integer;
    child_path character varying;
BEGIN
    --得到nodeid节点的路径
    select path,depth into parent_path, parent_depth from public.directsales_doubletrack where id=nodeid;
    child_depth := parent_depth + 1;
    --得到nodeid下的子节点，左或右
    select id into child_node_id from public.directsales_doubletrack where path like '%'||parent_path||'/%' and depth=child_depth and isright=is_right;
    --得到子节点的path信息
    select path into child_path from public.directsales_doubletrack where id=child_node_id;
    --得到子节点下的所有节点，即nodeid节点的所有is_right(左或右)节点，这边添加深度条件，求相同深度下，相同的节点
    RETURN query select id from public.directsales_doubletrack 
      where path like '%'||child_path||'%'
      and id <> nodeid
      and id not in (select node_id from public.directsales_nodehistory) 
      and id not in (select follow_id from public.directsales_nodehistory);
      
    RETURN;
END
$BODY$
  LANGUAGE plpgsql;
