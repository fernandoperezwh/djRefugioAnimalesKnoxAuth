# Manual de uso

Es importante identificar el valor de la variable `API_ENDPOINT` definida en el archivo __settings.py__ del proyecto. 
Esta variable se utiliza para realizar requests a los endpoints dentro del mismo proyecto. Por lo tanto, debe asegurarse
que se defina correctamente el host y el puerto.

```py
# ...

API_ENDPOINT = 'http://127.0.0.1:8010'
```
Si su proyecto corre en otro puerto deberá cambiar el valor de esta variable por el puerto correspondiente. 

Sin embargo, por default esta variable esta definida en la ip local `127.0.0.1` y en el puerto `8010` para utilizar por 
convención con el proyecto [djRefugioAnimaleCliente](https://github.com/fernandoperezwh/djRefugioAnimalesClient). 
Para más información, consulte la [documentación de djRefugioAnimaleCliente](https://github.com/fernandoperezwh/djRefugioAnimalesClient/blob/master/README.md)


## Session Authentication

Esta autentificación esta definida en el settings del proyecto. 
```py
REST_FRAMEWORK = {
    # ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication', 
        'rest_framework.authentication.TokenAuthentication', # <--- 
    ),
}
```
--- 
Al iniciar el proyecto podrá visualizar en el menu del navbar que los recursos de "Personas" y "Vacunas" se encuentran
protegidos. Esto se puede ver representado por el icono de candado (cuadro rojo de la siguiente imagen) y es debido a 
que aún no se cuenta con una sesión iniciada.
![home djRefugioAnimalesTokenAuthAPI](./media/01.png)

Para acceder al recurso protegido es necesario que inicie sesión llenando los datos en el formulario de login que puede
acceder al hacer clic en el boton que se encuentra en la esquina superior derecho (flecha roja de la imagen anterior).
![Formilario inicio de sesión](./media/02.png)

Al tener iniciada su sesión ahora podrá ser capaz de acceder a los recursos que ahora se encontraran desbloqueados y que
podrá ver representados al no tener ahora el icono del candado.
![Formilario inicio de sesión](./media/03.png)


## Token Authentication

Esta autentificación esta definida en el settings del proyecto. 
```py
REST_FRAMEWORK = {
    # ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication', # <--- 
        'rest_framework.authentication.TokenAuthentication',
    ),
}
```
--- 
Puede interactuar con el CRUD definidos en los [endpoints de la aplicación](./endpoints.md) haciendo requests.
Para ello, en todas las peticiones debera incluir la cabecera _"Authorization"_ cuyo valor corresponde al tipo de token
y el token de acceso o access_token.
```txt
"Authorization": "Token c6219db92d6c7b5a7d37e139286064683f9bf1ca"
```
### Obtener token mediante la interfaz de la aplicación
Puede obtener su access_token desde la interfaz de la aplicación siguiendo las siguientes indicaciones:
 1. Debe tener una sesión iniciada.
 2. En la vista de "home" podrá visualizar el boton _"Descubrir mi token"_, haga clic en el y a continuación descubrirá 
    su token.
    ![home Obtener token via home - button](./media/04.png)
    ![home Obtener token via home](./media/05.png)
### Obtener token mediante requests
Puede obtener su access_token realizando una petición `POST` al endpoint `api/auth/` pasando en el body un JSON que 
contenga su _"username"_ y _"password"_.

El siguiente cURL define lo comentado anteriormente. Puede utilizarlo como base, solo asegúrese de reemplazar los 
valores de: `<host>`, `<post>`, `<username>` y `<password>`
```bash
curl --location --request POST '<host>:<port>/api/auth/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "<username>",
    "password": "<password>"
}'
```

#### Ejemplo
```bash
curl --location --request POST 'localhost:8010/api/auth/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "fernando",
    "password": "fernando123"
}'
```
![home Obtener token via cURL](./media/06.png)


### Realizar request a un recurso protegido
Ahora que ya cuenta con su _"access_token"_ es capaz de consultar alguno de los recursos protegidos. 
A manera de ejemplo, realizaremos una consulta a la lista de personas. Sin embargo, la misma logica para la 
autentificación aplica para todos los endpoints de los modelos de la [lista de endpoints](./endpoints.md).

Para consultar la lista de personas se debe realizar una petición `GET` al endpoint `/api/persona/` y en los `headers`
debera incluir `Authorization: 'Token <access_token>'`.

El siguiente cURL define lo comentado anteriormente. Puede utilizarlo como base, solo asegúrese de reemplazar los 
valores de: `<host>`, `<post>`, y `<access_token>`

```bash
curl -v --location --request GET 'http://<host>:<port>/api/persona/' \
--header 'Authorization: Token <access_token>'
```

#### Ejemplo
```bash
curl -v --location --request GET 'http://localhost:8010/api/persona/' \
--header 'Authorization: Token c6219db92d6c7b5a7d37e139286064683f9bf1ca'
```
![home Consulta lista de personas via cURL](./media/07.png)
