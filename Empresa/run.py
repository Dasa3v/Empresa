from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# -------------------------------
# Configuración de la sesión y base de datos
# -------------------------------
app.config["SECRET_KEY"] = "clave_secreta_super_segura"
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/mi_base'  # Ajusta tu base de datos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Session(app)
db = SQLAlchemy(app)

# -------------------------------
# Modelo de usuario
# -------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

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
        user = User.query.filter_by(username=usuario).first()
        
        if user and check_password_hash(user.password, password):
            session["usuario"] = user.username  # Guardar usuario en sesión
            flash("Inicio de sesión exitoso", "success")
            return redirect(url_for("/dashboard"))
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
        hashed_password = generate_password_hash(password)
        
        existing_user = User.query.filter((User.username == usuario) | (User.email == email)).first()
        if existing_user:
            flash("El usuario o email ya existe", "warning")
        else:
            new_user = User(username=usuario, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            
            session["usuario"] = usuario  # Iniciar sesión automáticamente tras registrarse
            flash("Registro exitoso. Bienvenido, " + usuario, "success")
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
    return render_template('dashboard.html')

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
@app.route('/tienda')
def tienda():
    return render_template('tienda.html')


# -------------------------------
# Inicialización de la base de datos y ejecución del servidor
# -------------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
