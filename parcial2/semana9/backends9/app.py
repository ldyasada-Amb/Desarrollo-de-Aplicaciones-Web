from flask import Flask, render_template

app = Flask(__name__)


# Página principal
@app.route("/")
def home():
    return render_template("base.html")



# Página de productos
@app.route("/productos")
def productos():
    productos = [
        {
            "id": 1,
            "nombre": "Canguil",
            "precio": 2.50,
            "stock": 20
        },
        {
            "id": 2,
            "nombre": "Cola",
            "precio": 1.50,
            "stock": 30
        }
    ]

    return render_template(
        "productos.html",
        productos=productos
    )


# Página de clientes
@app.route("/clientes")
def clientes():
    return render_template("clientes.html")


# Página de proveedores
@app.route("/proveedores")
def proveedores():
    return render_template("proveedores.html")


# Página de facturación
@app.route("/facturacion")
def facturacion():
    return render_template("facturacion.html")


if __name__ == "__main__":
    app.run(debug=True)