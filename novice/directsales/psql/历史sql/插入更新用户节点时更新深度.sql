create OR REPLACE function set_depth() returns trigger as
$$
BEGIN
    IF NEW.parent_id is not null THEN
        select COALESCE(depth,0) + 1 into NEW.depth from directsales_doubletrack where id=NEW.parent_id;
    END IF;
    RETURN NEW;
END
$$
language plpgsql;

--create trigger set_depth before insert or update on
--public.directsales_doubletrack for each row execute procedure set_depth();

--SELECT id,parent_id,isright,depth FROM directsales_doubletrack where id=3


--UPDATE directsales_doubletrack SET depth='1327767776' where id=2

--select COALESCE(depth,0)+1 from directsales_doubletrack where id=3

