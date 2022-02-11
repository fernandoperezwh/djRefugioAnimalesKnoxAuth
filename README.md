# djRefugioAnimalesTokenAuthAPI

## Instalación
- Elegir una directorio de facil acceso para clonar el proyecto. 
    ```bash
    cd ~/Escritorio/
    ```
- Clonar el proyecto ya sea por ssh o https
    ```bash
    git clone git@github.com:fernandoperezwh/djRefugioAnimalesTokenAuthAPI.git
    ```
    ```bash
    git clone https://github.com/fernandoperezwh/djRefugioAnimalesTokenAuthAPI.git
    ```
- Crear un entorno virtual utilizando python 2.7
    ```bash
    mkvirtualenv djRefugioAnimalesTokenAuthAPI -p=2.7
    ```
- Activar el entorno creado en el anterior paso
    ```bash
    workon djRefugioAnimalesTokenAuthAPI
    ```
- Instalar las dependencias del archivo `requirements.txt` 
    ```bash
    pip install -r requirements.txt
    ```
- Realizar las migraciones del proyecto 
    ```bash 
    python manage.py migrate
    ```
- Cree un nuevo super usuario con el siguiente comando. Sugerimos que recuerde las credenciales de su usuario ya que los usaremos para autentificarnos en el proyecto y consumir los endpoints/recursos.
    ```bash
    python manage.py createsuperuser
    ```    
- Finalmente, ejecute el proyecto
    ```bash
    python manage.py runserver
    ```

## Uso

Este proyecto es un fork del proyecto principal djRefugioAnimales. 

En el proyecto existen tres modulos: Personas, Vacunas, Mascotas. El cual, cada uno de ellos tiene implementado un CRUD se consumen a traves de: Vistas basadas en funciones, vistas basadas en clases y API REST con Django REST Framework.

La parte importante de este proyecto consiste en el desarrollo de una API REST. Los endpoints expuestos se encuentran protegidos y, por lo tanto, requieren que se encuentre un usuario autentificado.

Este proyecto permite dos tipos de autentificación: por sesión y por token.