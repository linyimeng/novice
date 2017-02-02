-- Function: public.set_directpush_path()

-- DROP FUNCTION public.set_directpush_path();

CREATE OR REPLACE FUNCTION public.set_directpush_path()
  RETURNS trigger AS
$BODY$
DECLARE
    parent_directpush_path character varying;
BEGIN
    select directpush_path into parent_directpush_path from public.directsales_doubletrack where id=NEW.directpushuser_id;
    IF parent_directpush_path is null THEN
        NEW.directpush_path := '/' || NEW.id::character varying;
    ELSE
        NEW.directpush_path := parent_directpush_path || '/' || NEW.id;
    END IF;
    RETURN NEW;
END
$BODY$
  LANGUAGE plpgsql;

--create trigger set_directpush_path before insert or update on
--public.directsales_doubletrack for each row execute procedure set_directpush_path();



---test
--select * from directsales_doubletrack where directpush_path is null
