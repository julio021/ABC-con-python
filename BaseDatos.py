from psycopg2 import connect
host = "localhost"
port=5432
user ="ingenieria"
password= "manager"
dbname="bd_productos"

def cadenaConexion():
    conexion= connect(host=host,port=port,user=user,password=password,dbname=dbname)
    return conexion

