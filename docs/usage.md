# Manual de uso

Es importante identificar el valor de la variable `API_ENDPOINT` definida en el archivo __settings.py__ del proyecto. 
Esta variable se utiliza para realizar requests a los endpoints dentro del mismo proyecto. Por lo tanto, debe asegurarse
que se defina correctamente el host y el puerto.

```py
# ...

API_ENDPOINT = 'http://127.0.0.1:8010'
```
Por default esta variable esta definida en la ip local `127.0.0.1` y en el puerto `8010` para utilizar por convención con
el proyecto [djRefugioAnimaleCliente](https://github.com/fernandoperezwh/djRefugioAnimalesClient). Para más información,
consulte la siguiente [documentación]()


## Session Authentication

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

## Token Authentication

aaaa