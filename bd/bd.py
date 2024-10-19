from dotenv import load_dotenv
import mysql.connector
import os

# cargamos la variables del archivo .env
load_dotenv()

# atrapamos la variables de entorno
def __cnx():

    __BD = os.getenv("BD")
    __HOST = os.getenv("HOST")
    __PASSWORD = os.getenv("PASSWORD")
    __USERNAME = os.getenv("USER")

    #devolvemos la conexion
    return mysql.connector.connect(
        user = __USERNAME,
        passwd = __PASSWORD,
        host = __HOST,
        database = __BD,
    )

CNX = __cnx()