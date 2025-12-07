from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="db-api",
        user="root",
        password="root",
        database="api_db"
    )

class Temperature(BaseModel):
    celsius: float

@app.post("/convert/")
def convert_temperature(data: Temperature):
    fahrenheit = (data.celsius * 9/5) + 32

    # Guardar en base de datos
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO temperature_logs (celsius, fahrenheit)
        VALUES (%s, %s)
    """
    cursor.execute(query, (data.celsius, fahrenheit))
    conn.commit()

    cursor.close()
    conn.close()

    return {
        "celsius": data.celsius,
        "fahrenheit": fahrenheit
    }
