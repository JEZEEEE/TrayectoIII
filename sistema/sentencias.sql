
CREATE OR REPLACE FUNCTION public.eliminar_usuario_logicamente(
	p1_cod_usu integer)
    RETURNS void
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
BEGIN
    UPDATE public.sistema_usuario SET est_usu = 'I' WHERE cod_usu = p1_cod_usu AND est_usu = 'A';
END;
$BODY$;

ALTER FUNCTION public.eliminar_usuario_logicamente(integer)
    OWNER TO postgres;





-- FUNCTION: public.modificar_usuario(integer, character varying, character varying, integer, integer, character)

-- DROP FUNCTION IF EXISTS public.modificar_usuario(integer, character varying, character varying, integer, integer, character);

CREATE OR REPLACE FUNCTION public.modificar_usuario(
	p1_cod_usu integer,
	p2_cor_usu character varying,
	p3_con_usu character varying,
	p4_fky_per integer,
	p5_fky_rol integer,
	p6_est_usu character)
    RETURNS integer
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE
resultado integer;
BEGIN
    UPDATE public.sistema_usuario SET cor_usu = p2_cor_usu, con_usu = p3_con_usu, fky_per_id = p4_fky_per, fky_rol_id = p5_fky_rol, est_usu = p6_est_usu 
	WHERE cod_usu = p1_cod_usu RETURNING cod_usu INTO resultado;
	
	RETURN resultado;
END;
$BODY$;

ALTER FUNCTION public.modificar_usuario(integer, character varying, character varying, integer, integer, character)
    OWNER TO postgres;
