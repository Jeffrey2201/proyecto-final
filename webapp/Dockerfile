# -----------------------------
# Dockerfile para webapp
# -----------------------------
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos de la aplicación
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir flask mysql-connector-python requests

# Exponer puerto 80
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
