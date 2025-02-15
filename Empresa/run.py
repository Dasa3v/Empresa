from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)

# Configuración de la sesión
app.config["SECRET_KEY"] = "clave_secreta_super_segura"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", endpoint="home")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        # Simulación de usuario en la base de datos
        if usuario == "admin" and password == "1234":
            session["usuario"] = usuario  # Guardar usuario en la sesión
            return redirect(url_for("dashboard"))  # Redirigir al dashboard

        return render_template("login.html", mensaje="Usuario o contraseña incorrectos")

    return render_template("login.html")

@app.route("/registro", methods=["GET", "POST"], endpoint="registro")
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        email = request.form["email"]
        password = request.form["password"]
        # Aquí se guardará en la base de datos (próximamente)
        return redirect(url_for("login"))  # Redirigir al login después del registro

    return render_template("registro.html")

@app.route("/recuperacion", methods=["GET", "POST"], endpoint="recuperacion")
def recuperacion():
    if request.method == "POST":
        email = request.form["email"]
        # Aquí se implementará el sistema de recuperación (próximamente)
        return render_template("recuperacion.html", mensaje="Si el correo existe, recibirás instrucciones.")

    return render_template("recuperacion.html")

@app.route("/dashboard", endpoint="dashboard")
def dashboard():
    if "usuario" in session:
        return render_template("dashboard.html")
    return redirect(url_for("login"))

@app.route("/logout", endpoint="logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("home"))

@app.route("/index", endpoint="index")
def index():
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
