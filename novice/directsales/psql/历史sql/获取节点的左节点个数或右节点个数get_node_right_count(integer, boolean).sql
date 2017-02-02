-- Function: public.get_node_right_count(integer, boolean)

-- DROP FUNCTION public.get_node_right_count(integer, boolean);

-- DROP FUNCTION public.get_node_right_count(integer);

--得到节点的右节点或左节点个数
CREATE OR REPLACE FUNCTION public.get_node_child_count(
    nodeid integer,
    is_right boolean)
  RETURNS integer AS
$BODY$
Declare
first_child_id integer;
node_right_count integer;
BEGIN
    SELECT id into first_child_id from public.directsales_doubletrack as dd where dd.isright = is_right and parent_id = nodeid;
    WITH RECURSIVE child
    AS (
     SELECT id
     FROM public.directsales_doubletrack
     WHERE id=first_child_id
     UNION ALL
    SELECT dd.id
    FROM public.directsales_doubletrack AS dd
    INNER JOIN child 
    ON child.id = dd.parent_id
    )
    select count(id) into node_right_count FROM child;
    RETURN node_right_count;
END
$BODY$
  LANGUAGE plpgsql;

--得到节点的总节点个数
  CREATE OR REPLACE FUNCTION public.get_node_child_count(
    nodeid integer
    )
  RETURNS integer AS
$BODY$
Declare
node_child_count integer;
BEGIN
    WITH RECURSIVE child
    AS (
     SELECT id
     FROM public.directsales_doubletrack
     WHERE id=nodeid
     UNION ALL
    SELECT dd.id
    FROM public.directsales_doubletrack AS dd
    INNER JOIN child 
    ON child.id = dd.parent_id
    )
    select count(id) - 1 into node_child_count FROM child;
    RETURN node_child_count;
END
$BODY$
  LANGUAGE plpgsql;
