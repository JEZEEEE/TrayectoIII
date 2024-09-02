# queries.py
from django.db import connection

def obtener_usuarios():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM public.listar_usuarios() where est_usu='A'")
        columns = [col[0] for col in cursor.description]
        result = cursor.fetchall()
        # Para depuración: imprime los datos obtenidos
        print(f"Resultado de la consulta: {result}")
        return [
            dict(zip(columns, row))
            for row in result
        ]

def eliminar_usuario_logicamente(cod_usu):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE public.sistema_usuario SET est_usu = 'I' WHERE cod_usu = %s AND est_usu = 'A'", [cod_usu])
        
def modificar_usuario(cod_usu, cor_usu, con_usu, fky_per, fky_rol, est_usu):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT public.modificar_usuario(%s, %s, %s, %s, %s, %s)
        """, [cod_usu, cor_usu, con_usu, fky_per, fky_rol, est_usu])
        result = cursor.fetchone()
        return result[0] if result else None