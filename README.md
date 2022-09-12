# YODA API

## Instalación

1. Creamos un entonro virtual de Python con `virtualenv venv` o `python -m venv ./venv`
2. Instalamos los requisitos con `pip install -r requirements,txt`

## Ejecuta el servidor en local

---

Entramos en la carpeta src: `cd src`

> Para desarrollo

`uvicorn main:app --reload --port 8000` or `python dev.py`

> Para producción

`uvicorn main:app --port 8000`

## Ejecuta en local con Docker

---

1. Construye la imagen con `docker build -t yoda-api .`
2. Ejecútalo: `docker run -e PORT=8000 --env-file .env yoda-api`
3. Accede desde el navegador en `http://localhost:8000`

## Ejecución en la nube

---

Comando: `gunicorn -w 4 -k gevent -t 120 main:app`
