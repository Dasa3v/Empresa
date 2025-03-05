from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session

app = Flask(__name__)
app.config["SECRET_KEY"] = "clave_secreta_super_segura"
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

@app.route("/", endpoint="home")
def home():
    usuario = session.get("usuario")
    return render_template("home.html", usuario=usuario)

@app.route("/login", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        if usuario == "admin" and password == "admin":
            session["usuario"] = usuario
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Usuario o contraseña incorrectos", "danger")
    return render_template("login.html")

@app.route("/registro", methods=["GET", "POST"], endpoint="registro")
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        email = request.form["email"]
        password = request.form["password"]
        flash("Registro exitoso. Bienvenido, " + usuario, "success")
        session["usuario"] = usuario
        return redirect(url_for("home"))
    return render_template("registro.html")

@app.route("/recuperacion", methods=["GET", "POST"], endpoint="recuperacion")
def recuperacion():
    if request.method == "POST":
        flash("Si el correo existe, recibirás instrucciones.", "info")
    return render_template("recuperacion.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/logout", endpoint="logout")
def logout():
    session.pop("usuario", None)
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for("home"))

@app.route("/tienda")
def tienda():
    return render_template("tienda_clientes.html")

@app.route("/cuidadores")
def cuidadores():
    return render_template("cuidadores.html")

@app.route("/veterinaria")
def veterinaria():
    return render_template("veterinaria.html")

@app.route("/citas")
def citas():
    return render_template("citas.html")

# -------------------------------
# Rutas de productos
# -------------------------------
@app.route("/productos")
def productos():
    """Página principal de productos."""
    return render_template("productos.html")

# -------------------------------
# Rutas de productos gatos
# -------------------------------

@app.route("/productos/gatos", endpoint="productos_gatos")
def productos_gatos():
    return render_template("gatos.html")


# -------------------------------
# Rutas de perros
# -------------------------------

@app.route("/productos/perros", endpoint="productos_perros")
def productos_perros():
    """Página específica de productos para perros."""
    return render_template("perros.html")

# -------------------------------
# Rutas de otros
# -------------------------------

@app.route("/productos/otros", endpoint="productos_otros")
def productos_otros():
    """Página específica de productos para otros animales."""
    return render_template("otros.html")

# -------------------------------
# Ejecución del servidor
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)
