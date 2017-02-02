-- Function: public.get_node_child_count_recursion(integer, boolean)

-- DROP FUNCTION public.get_node_child_count_recursion(integer, boolean);

CREATE OR REPLACE FUNCTION public.get_node_child_count(
    nodeid integer,
    is_right boolean)
  RETURNS integer AS
$BODY$
Declare
node_path character varying;
node_right_count integer;
BEGIN
    SELECT * from public.directsales_doubletrack as dd where dd.isright = is_right and parent_id = nodeid;

END
$BODY$
  LANGUAGE plpgsql;
