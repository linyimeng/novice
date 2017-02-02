create or replace function get_txt_count(p_source_txt character varying, p_count_txt character varying)
returns integer
as $get_txt_count$
declare
v_idx integer := 1;
v_cnt integer := 0;
v_source_txt character varying(2000) := p_source_txt;
v_len integer := length(p_count_txt);
begin
   while v_idx > 0 loop
       v_idx := position(p_count_txt in v_source_txt);
       if v_idx > 0 then
           v_cnt := v_cnt + 1;
           v_source_txt := right(v_source_txt, length(v_source_txt) - v_idx - v_len + 1);
       end if;
   end loop;
   return v_cnt;
end;
$get_txt_count$ language plpgsql;