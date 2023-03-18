from BaseDatos import cadenaConexion

def listadoProductos():
    sql = "SELECT * FROM productos"
    conn = cadenaConexion()
    cur= conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result

def listarProductos(id):
    sql = "SELECT * FROM productos WHERE id =%s"
    conn = cadenaConexion()
    cur= conn.cursor()
    cur.execute(sql,(id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

def guardarProducto( nombre, descripcion, cantidad, precio,categoria):
    sql = "INSERT INTO productos (id,nombre, descripcion, cantidad, precio,categoria)VALUES(%s,%s,%s,%s,%s)"
    conn = cadenaConexion()
    cur= conn.cursor()
    cur.execute(sql,(nombre, descripcion, cantidad, precio,categoria))
    conn.commit()
    cur.close()
    conn.close()
    return "Producto Guardado"


def actualizarProducto(id,nombre,descripcion, cantidad, precio,categoria):
    sql = "UPDATE productos SET id=%s,nombre=%s, descripcion=%s, cantidad=%s, precio=%s,categoria=%s WHERE id=%s"
    conn = cadenaConexion()
    cur= conn.cursor()
    cur.execute(sql,( nombre, descripcion, cantidad, precio,categoria,id))
    conn.commit()
    cur.close()
    conn.close()
    return "Producto Actualizado"

def eliminarProductos(id):
    sql = "DELETE * FROM productos  WHERE id =%s"
    conn = cadenaConexion()
    cur= conn.cursor()
    cur.execute(sql,(id,))
    conn.commit()
    cur.close()
    conn.close()
    return "PRODUCTO ELIMINADO"

























     
