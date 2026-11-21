# Parcial final - Programas universitarios

Formulario de Django para registrar programas universitarios en `/programas/crear/`.
La base de datos incluida contiene cinco programas de ejemplo.

## Ejecutar el proyecto

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Para entrar al administrador en `/admin/`, crea un usuario con
`python manage.py createsuperuser`.

## Publicar en PythonAnywhere

Sigue la guía entregada por el docente: clona este repositorio, crea un entorno
virtual con Python 3.13 e instala los requisitos. Crea una aplicación web con
configuración manual y selecciona ese entorno virtual. En el archivo WSGI, usa
la ruta de la carpeta clonada y `my_project.settings`.

En `my_project/settings.py` del servidor, cambia `DEBUG` a `False` y agrega
`TU_USUARIO.pythonanywhere.com` a `ALLOWED_HOSTS`. Ejecuta
`python manage.py migrate` y `python manage.py collectstatic --noinput`.
En la pestaña Web, configura `/static/` hacia la carpeta `static_publico` del
repositorio y pulsa **Reload**. Comprueba `/programas/crear/` y `/admin/`.
