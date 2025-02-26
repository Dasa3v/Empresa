import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",  # Reemplaza con tu usuario real
        password="",  # Deja esto vacío si no tiene contraseña
        database="mi_base"
    )
    print("Conexión exitosa a la base de datos")
except mysql.connector.Error as err:
    print(f"Error al conectar: {err}")
