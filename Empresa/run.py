from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session

app = Flask(__name__)

# -------------------------------
# Configuración de la sesión
# -------------------------------
app.config["SECRET_KEY"] = "clave_secreta_super_segura"
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# -------------------------------
# Ruta principal (Home)
# -------------------------------
@app.route("/", endpoint="home")
def home():
    usuario = session.get("usuario")
    return render_template("home.html", usuario=usuario)

# -------------------------------
# Ruta de inicio de sesión (Login)
# -------------------------------
@app.route("/login", methods=["GET", "POST"], endpoint="login")
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        
        # Simulación de autenticación sin base de datos
        if usuario == "admin" and password == "admin":
            session["usuario"] = usuario  # Guardar usuario en sesión
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Usuario o contraseña incorrectos", "danger")
    return render_template("login.html")

# -------------------------------
# Ruta de registro (Registro de usuario)
# -------------------------------
@app.route("/registro", methods=["GET", "POST"], endpoint="registro")
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        email = request.form["email"]
        password = request.form["password"]
        
        # Simulación de registro sin base de datos
        flash("Registro exitoso. Bienvenido, " + usuario, "success")
        session["usuario"] = usuario  # Iniciar sesión automáticamente tras registrarse
        return redirect(url_for("home"))
    return render_template("registro.html")

# -------------------------------
# Ruta de recuperación de contraseña
# -------------------------------
@app.route("/recuperacion", methods=["GET", "POST"], endpoint="recuperacion")
def recuperacion():
    if request.method == "POST":
        flash("Si el correo existe, recibirás instrucciones.", "info")
    return render_template("recuperacion.html")

# -------------------------------
# Ruta del Dashboard
# -------------------------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# -------------------------------
# Ruta de cierre de sesión (Logout)
# -------------------------------
@app.route("/logout", endpoint="logout")
def logout():
    session.pop("usuario", None)
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for("home"))

# -------------------------------
# Ruta de la tienda
# -------------------------------
@app.route("/tienda")
def tienda():
    return render_template("tienda.html")

# -------------------------------
# Ruta de cuidadores
# -------------------------------
@app.route("/cuidadores")
def cuidadores():
    return render_template("cuidadores.html")

# -------------------------------
# Ruta de veterinaria
# -------------------------------
@app.route("/veterinaria")
def veterinaria():
    return render_template("veterinaria.html")

# -------------------------------
# Ruta de citas
# -------------------------------
@app.route("/citas")
def citas():
    return render_template("citas.html")

# -------------------------------
# Ruta de productos
# -------------------------------
@app.route("/productos")
def productos():
    return render_template("productos.html")





# -------------------------------
# Ejecución del servidor
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
