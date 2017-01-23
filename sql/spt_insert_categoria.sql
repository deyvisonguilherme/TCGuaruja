CREATE OR REPLACE FUNCTION spt_insert_categoria(v_categoria varchar(25)) RETURNS VOID AS $$
DECLARE
	exist INTEGER;
BEGIN
    exist = (SELECT count(nm_categoria) from categorias where nm_categoria = v_categoria);

    IF exist > 0 THEN
	    RAISE 'Unique violado!';
    ELSE
	    INSERT INTO categorias(id, nm_categoria) values (nextval('categorias_id_seq'), v_categoria);
    END IF;

END;
$$ LANGUAGE 'plpgsql';