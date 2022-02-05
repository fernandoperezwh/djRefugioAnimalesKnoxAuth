# djRefugioAnimalesTokenAuthAPI
Aplicación servidor del proyecto [djRefugioAnimalesTokenAuthClient](https://github.com/fernandoperezwh/djRefugioAnimalesTokenAuthClient), es necesario ejecutar ambos proyectos para su correcto funcionamiento.

En este proyecto se muestra la autentificacion por [TokenAuthentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)


# Instalación
- Elegir una directorio de facil acceso para clonar el proyecto. 
    ```bash
    cd ~/Escritorio/
    ```
- Clonar el proyecto ya sea por ssh o https
    ```bash
    # Clone via ssh
    git clone git@github.com:fernandoperezwh/djRefugioAnimalesTokenAuthAPI.git
    # Clone via https
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
- Opcionalmente puede crear un nuevo super usuario con el siguiente comando
    ```bash
    python manage.py createsuperuser
    ```    
    Igualmente puede usar las siguientes credenciales de un superusuario de prueba existente
    - user: `fernando`
    - passwd: `fernando123`

<!-- - Crear super user con: ```python manage.py createsuperuser``` -->
- Finalmente, ejecute el proyecto
    ```bash
    python manage.py runserver
    ```

