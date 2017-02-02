priority

-- Function: public.set_priority_doubletrack()

-- DROP FUNCTION public.set_priority_doubletrack();

CREATE OR REPLACE FUNCTION public.set_priority_doubletrack()
  RETURNS trigger AS
$BODY$
BEGIN
    IF NEW.identity = 1 THEN
        NEW.priority := 10;
    ELSIF NEW.identity = 2 THEN
        NEW.priority := 30;
    ELSIF NEW.identity = 3 THEN
        NEW.priority := 100;
    ELSIF NEW.identity = 4 THEN
        NEW.priority := 300;
    END IF;
    RETURN NEW;
END
$BODY$
  LANGUAGE plpgsql;

--create trigger set_priority_doubletrack before insert on
--public.directsales_doubletrack for each row execute procedure set_priority_doubletrack();
