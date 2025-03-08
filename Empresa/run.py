# Importación de módulos necesarios de Flask y Flask-Session
from flask import Flask, render_template, request, redirect, url_for, session, flash, current_app
from flask_session import Session

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Configuración de la aplicación
app.config["SECRET_KEY"] = "clave_secreta_super_segura"  # Clave secreta para sesiones y seguridad
app.config["SESSION_TYPE"] = "filesystem"                # Almacenamiento de sesiones en el sistema de archivos

# Inicialización de las sesiones
Session(app)

# -------------------------------
# Rutas de la aplicación
# -------------------------------

# Ruta principal (Home)
@app.route("/", endpoint="home")
def home():
    # Obtiene el usuario de la sesión (si existe)
    usuario = session.get("usuario")
    # Renderiza la plantilla 'home.html' pasando el usuario
    return render_template("home.html", usuario=usuario)

# Ruta de inicio de sesión (Login)
@app.route("/login", methods=["GET", "POST"], endpoint="login")
def login():
    # Si se envía el formulario (método POST), se procesa el login
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        # Validación simple: si las credenciales son "admin", se inicia la sesión
        if usuario == "admin" and password == "admin":
            session["usuario"] = usuario  # Guarda el usuario en la sesión
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Usuario o contraseña incorrectos", "danger")
    # Si es GET o hay error en la validación, muestra el formulario de login
    return render_template("login.html")

# Ruta de registro de usuarios
@app.route("/registro", methods=["GET", "POST"], endpoint="registro")
def registro():
    # Si se envía el formulario de registro (POST), se procesa el registro
    if request.method == "POST":
        usuario = request.form["usuario"]
        email = request.form["email"]
        password = request.form["password"]
        flash("Registro exitoso. Bienvenido, " + usuario, "success")
        session["usuario"] = usuario  # Inicia sesión con el nuevo usuario
        return redirect(url_for("home"))
    # Si es GET, se muestra el formulario de registro
    return render_template("registro.html")

# Ruta de recuperación de contraseña
@app.route("/recuperacion", methods=["GET", "POST"], endpoint="recuperacion")
def recuperacion():
    # Si se envía el formulario (POST), muestra un mensaje informativo
    if request.method == "POST":
        flash("Si el correo existe, recibirás instrucciones.", "info")
    # Renderiza la plantilla de recuperación de contraseña
    return render_template("recuperacion.html")

# Ruta del Dashboard (Panel principal tras login)
@app.route("/dashboard")
def dashboard():
    # Renderiza la plantilla 'dashboard.html'
    return render_template("dashboard.html")

# Ruta para cerrar sesión (Logout)
@app.route("/logout", endpoint="logout")
def logout():
    # Elimina el usuario de la sesión y muestra un mensaje de éxito
    session.pop("usuario", None)
    flash("Sesión cerrada exitosamente", "success")
    return redirect(url_for("home"))

# Ruta de la tienda para clientes
@app.route("/tienda")
def tienda():
    # Renderiza la plantilla 'tienda_clientes.html'
    return render_template("tienda_clientes.html")

# Ruta de la sección de cuidadores
@app.route("/cuidadores")
def cuidadores():
    # Renderiza la plantilla 'cuidadores.html'
    return render_template("cuidadores.html")

# Ruta de la sección de veterinaria
@app.route("/veterinaria")
def veterinaria():
    # Renderiza la plantilla 'veterinaria.html'
    return render_template("veterinaria.html")

# Ruta de la sección de citas
@app.route("/citas")
def citas():
    # Renderiza la plantilla 'citas.html'
    return render_template("citas.html")

# -------------------------------
# Rutas de productos
# -------------------------------

# Página principal de productos
@app.route("/productos")
def productos():
    """Página principal de productos."""
    return render_template("productos.html")

# Página específica de productos para gatos
@app.route("/productos/gatos", endpoint="productos_gatos")
def productos_gatos():
    # Renderiza la plantilla 'gatos.html'
    return render_template("gatos.html")

# Página específica de productos para perros
@app.route("/productos/perros", endpoint="productos_perros")
def productos_perros():
    """Página específica de productos para perros."""
    return render_template("perros.html")

# Página específica de productos para otros animales
@app.route("/productos/otros", endpoint="productos_otros")
def productos_otros():
    """Página específica de productos para otros animales."""
    return render_template("otros.html")

# -------------------------------
# Ejecución del servidor
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
