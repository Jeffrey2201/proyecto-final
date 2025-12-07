-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS webapp_db;

-- Usar la base de datos
USE webapp_db;

-- Crear la tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Si quieres agregar un usuario inicial (opcional)
INSERT INTO users (username, password) VALUES ('admin', 'admin123');
