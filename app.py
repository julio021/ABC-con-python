from flask import Flask,jsonify, request, send_file
import rutas
app= Flask(__name__)

@app.get('/api/productos')
def getProductos():
    data = rutas.listadoProductos()
    return jsonify(data)

    
@app.get("/api/productos/<id>")
def getProducto(id):
    data = rutas.listarProductos(id)
    return jsonify(data)

@app.post('/api/productos')
def postProducto():
    producto = request.json
    if request.method == "POST":
        nombre= producto["nombre"]
        descripcion= producto["descripcion"] 
        cantidad= producto["cantidad"] 
        precio= producto["precio"] 
        categoria= producto["categoria"] 
       
    data = rutas.guardarProducto(nombre,descripcion, cantidad, precio,categoria)
    return jsonify(data)

@app.put('/api/productos/<id>')
def putProducto(id):
    producto = request.json
    if request.method == "PUT":
        nombre = producto["nombre"] 
        descripcion= producto["descripcion"] 
        cantidad= producto["cantidad"] 
        precio= producto["precio"] 
        categoria= producto["categoria"] 

    data = rutas.actualizarProducto(id,nombre,descripcion, cantidad, precio,categoria)
    return jsonify(data)


@app.delete('/api/productos/<id>')
def deleteProducto(id):
    data = rutas.eliminarProductos(id)
    return jsonify(data)

    

@app.get("/")
def index ():
    return send_file("static/index.html")

if __name__ =="__main__":
    app.run(host="127.0.0.1", port=5500)


