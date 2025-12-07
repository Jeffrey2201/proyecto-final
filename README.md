# proyecto-final
proyecto basico

# Proyecto2 - Suite WebApp con API y Docker

Este proyecto consiste en una **suite de aplicaciones** desarrolladas con **Flask** (WebApp), **FastAPI** (API), y **MySQL** para las bases de datos. Todo el proyecto se ejecuta usando **Docker** y **docker-compose**.

---

## Estructura del proyecto

```

proyecto2/
├── webapp/
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       ├── calculator.html
│       ├── index.html
│       ├── login.html
│       └── register.html
├── api/
│   ├── main.py
│   └── requirements.txt
├── db-web/
│   └── init.sql
├── db-api/
│   └── init.sql
├── docker-compose.yml
└── README.md

````

---

## Tecnologías utilizadas

- **Flask** → WebApp con sistema de login y calculadora de conversión de Celsius a Fahrenheit.  
- **FastAPI** → API para realizar la conversión de temperatura.  
- **MySQL 5.7** → Bases de datos para WebApp (`webapp_db`) y API (`api_db`).  
- **Docker & Docker-Compose** → Contenerización de toda la suite.  
- **Adminer** → Gestión de bases de datos vía web.  

---

## Servicios

1. **WebApp (Flask)**  
   - Puerto: `80`  
   - Funcionalidades: registro de usuario, login, calculadora de temperatura.  
   - Conecta a la base de datos `webapp_db`.  
   - Llama a la API para convertir temperatura.  

2. **API (FastAPI)**  
   - Puerto: `8000`  
   - Funcionalidad: recibe temperatura en Celsius y devuelve Fahrenheit.  
   - Conecta a la base de datos `api_db` para registrar conversiones (si se implementa logging).  

3. **Bases de datos MySQL**  
   - `db-web` → `webapp_db`  
   - `db-api` → `api_db`  

4. **Adminer**  
   - Puerto: `8080`  
   - Herramienta web para gestionar MySQL.  

---

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

```
git clone https://github.com/Jeffrey2201/proyecto-final.git
cd proyecto2
````

2. Construir y levantar los contenedores:

```
sudo docker-compose up --build -d
```

3. Verificar que los contenedores estén corriendo:

```
sudo docker ps
```

4. Acceder a los servicios:

* WebApp: [http://localhost](http://localhost)
* API: [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger de FastAPI)
* Adminer: [http://localhost:8080](http://localhost:8080)

---

## Datos de acceso a MySQL

* Host: `db-web` / `db-api`
* Usuario: `root`
* Contraseña: `root`
* Bases de datos: `webapp_db` y `api_db`

---

## Notas

* Asegúrate de que los puertos `80`, `8000` y `8080` estén libres en tu máquina antes de ejecutar Docker.
* Todos los cambios de las bases de datos se conservan si se usan volúmenes Docker correctamente.
* El WebApp llama a la API vía Docker network usando el nombre del servicio (`api`) como host.

---

## Autor

**Jeffrey Castro**
[GitHub](https://github.com/Jeffrey2201)


