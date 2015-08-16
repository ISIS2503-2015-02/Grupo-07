# Grupo-07
Repositorio de código del grupo 07 de Arquitectura y Diseño de Software, Universidad de los Andes, 2015-20.

### Instalación
Deben tener virtualenv instalado globalmente:
```sh
$ [sudo] pip install virtualenv
```

Creen un entorno virtual llamado venv, este contendrá las dependencias requeridas para correr el proyecto de manera satisfactoria y evitará inconvenientes con las versiones:
```sh
$ virtualenv venv
```

Asegurense de activar su ambiente virtual:
```sh
$ source venv/bin/activate
```

Pueden desactivar el ambiente virtual en cualquier momento usando:
```sh
$ deactivate
```

El repositorio contiene un archivo generado por *pip* llamado **requirements.txt**, este contiene las dependencias necesarias para correr el proyecto junto a sus respectivas versiones. Pueden utilizar *pip* para instalar el contenido de este archivo:
```sh
$ pip install -r requirements.txt
```

Es necesario tener instaladas las librerias requeridas por *GeoDjango*, las instrucciones para Mac y Windows se encuentran en este enlace:
- [GeoDjango Installation](https://docs.djangoproject.com/en/1.8/ref/contrib/gis/install/)

### Uso

Sobre *gunicorn*:
```sh
$ gunicorn -c gunicorn.py.ini tbcSite.wsgi
```

También pueden correrlo de forma local con *Heroku*, este iniciara el contenido de **Procfile**:
```sh
$ heroku local
```

Sobre *uWSGI*:
```sh
$ uwsgi --ini uwsgi.py.ini
```

### Saltar autenticación

Reemplacen el archivo **login.html** de *Django* por el archivo de mismo nombre que está en el folder **recursos_Django** del proyecto. Pueden hacer esto desde consola ubicados en la raíz del proyecto:
```sh
mv recursos_Django/login.html venv/lib/python2.7/site-packages/django/contrib/admin/templates/admin/
```

Reemplacen el archivo **middleware.py** de *Django* por el archivo de mismo nombre que está en el folder "recursos_Django" del proyecto. Pueden hacer esto desde consola ubicados en la raíz del proyecto:
```sh
mv recursos_Django/middleware.py venv/lib/python2.7/site-packages/django/contrib/auth/
```

De lo contrario cualquier *HTTP request* va a devolver la página de login. Una vez reemplacen los archivos van a estar autenticados permanentemente como *ramirezamayas*.