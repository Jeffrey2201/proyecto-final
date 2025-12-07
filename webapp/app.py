from flask import Flask, render_template, request, redirect, session
import mysql.connector
import os
import requests   # <-- Necesario para comunicar con la API

app = Flask(__name__)
app.secret_key = "supersecretkey"

API_URL = "http://api:8000/convert/"   # <-- URL del contenedor API


# -----------------------------
# CONEXIÓN A LA BASE DE DATOS
# -----------------------------
def create_db_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )


# -----------------------------
# RUTA RAÍZ
# -----------------------------
@app.route('/')
def home():
    if "username" in session:
        return redirect("/calculator")
    return redirect('/login')


# -----------------------------
# LOGIN
# -----------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = None

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        try:
            connection = create_db_connection()
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
            user = cursor.fetchone()

            cursor.close()
            connection.close()

            if user:
                session["username"] = username
                return redirect("/")
            else:
                msg = "❌ Usuario o contraseña incorrectos."

        except Exception as e:
            msg = f"Error: {e}"

    return render_template("login.html", message=msg)


# -----------------------------
# REGISTRO
# -----------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None

    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            message = "Debes llenar todos los campos."
            return render_template("register.html", message=message)

        try:
            connection = create_db_connection()
            cursor = connection.cursor(buffered=True)

            # Verificar si el usuario ya existe
            cursor.execute("SELECT id FROM users WHERE username=%s", (username,))
            existing = cursor.fetchone()

            if existing:
                message = "⚠️ El usuario ya está registrado. Prueba con otro."
                cursor.close()
                connection.close()
                return render_template("register.html", message=message)

            # Insertar nuevo usuario
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password)
            )
            connection.commit()

            cursor.close()
            connection.close()

            message = "✅ Usuario registrado con éxito."

        except Exception as e:
            message = f"❌ Error en la base de datos: {e}"

    return render_template("register.html", message=message)


# -----------------------------
# CALCULADORA
# -----------------------------
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if "username" not in session:
        return redirect("/login")

    result = None

    if request.method == 'POST':
        temp = request.form.get("temperature")

        if temp:
            try:
                # -----------------------------
                # Llamada al API (en vez de calcular localmente)
                # -----------------------------
                response = requests.post(API_URL, json={"celsius": float(temp)})

                if response.status_code == 200:
                    data = response.json()
                    result = data["fahrenheit"]  # El resultado viene del API
                else:
                    result = "Error en la API"

            except Exception as e:
                print("ERROR LLAMANDO AL API:", e)
                result = "No se puede conectar al API"

    return render_template("calculator.html", result=result, username=session["username"])


# -----------------------------
# LOGOUT
# -----------------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# -----------------------------
# RUN
# -----------------------------
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)  # <-- Mantener el puerto 80
