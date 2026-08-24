from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, serviddor iniciado en la raiza!"

@app.route("/productos")
def productos():
    return "¡Hola, productos !"

@app.route("/productosId")
def prodcutosId():
    return "¡Hola, productosId!"

@app.route("/clientes")
def clientes():
    return "¡Hola, clientes!"

@app.route("/proveedores")
def proveedores():
    return "¡Hola, proveedores!"

@app.route("/facturacion")
def facturacion():
    return "¡Hola, facturacion!"



if __name__ == "__main__":
    app.run(debug=True)
    