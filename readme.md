# InstaConquer

Este proyecto fue desarrollado como parte del Máster en Desarrollo Web Full Stack en ConquerBlocks. InstaConquer es una mini red social construida con Django que permite a los usuarios compartir fotos, seguir a otros usuarios y comentar en las publicaciones. Queremos expresar nuestro agradecimiento a ConquerBlocks por su apoyo y orientación durante este proyecto.

## Descripción

InstaConquer es una aplicación web que ofrece las siguientes funcionalidades:

- Registro y autenticación de usuarios.
- Publicación de fotos.
- Seguir y dejar de seguir a otros usuarios.
- Comentar en las publicaciones.
- Ver el feed de publicaciones de los usuarios seguidos.
- Editar perfil de usuario.

## Requisitos

- Python 3.x
- Django 3.x
- SQLite (o cualquier otro gestor de base de datos soportado por Django)
- Virtualenv (opcional, pero recomendado)

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Alvaro-Alonso-Portillo/instaconquer.git
    cd instaconquer
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

3. Instala las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

5. Carga datos iniciales (opcional):
    ```bash
    python manage.py loaddata initial_data.json
    ```

6. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

7. Abre tu navegador y visita `http://127.0.0.1:8000` para ver la aplicación en acción.

## Modelos
### Usuario
-Nombre de usuario

-Correo electrónico

-Contraseña

-Foto de perfil

-Biografía

### Publicación
-Imagen

-Descripción

-Fecha de publicación

-Autor (relación ForeignKey con el modelo Usuario)

### Comentario
-Texto

-Fecha de publicación

-Autor (relación ForeignKey con el modelo Usuario)

-Publicación (relación ForeignKey con el modelo Publicación)


## Contribuciones
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

-Haz un fork del repositorio.

-Crea una rama nueva (git checkout -b feature/nueva-funcionalidad).

-Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').

-Sube los cambios a tu fork (git push origin feature/nueva-funcionalidad).

-Abre un pull request en GitHub.

## Agradecimientos
Quiero agradecer a ConquerBlocks por su apoyo y guía durante el desarrollo de este proyecto. Su dedicación y recursos han sido fundamentales para nuestro aprendizaje y éxito.


