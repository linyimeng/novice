create OR REPLACE function set_path() returns trigger as
$$
BEGIN
    IF NEW.parent_id is not null THEN
        select COALESCE(path,'') || '/' || NEW.id into NEW.PATH from public.directsales_doubletrack where id=NEW.parent_id;
    ELSE
        NEW.path := '/' || NEW.id::character varying;
    END IF;
    RETURN NEW;
END
$$
language plpgsql;

--create trigger set_path before insert or update on
--public.directsales_doubletrack for each row execute procedure set_path();

--SELECT id,parent_id,isright,depth,path FROM directsales_doubletrack where id=1
--update directsales_doubletrack set 



