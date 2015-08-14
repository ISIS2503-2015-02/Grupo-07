# Grupo-07
Repositorio de código del grupo 07 de Arquitectura y Diseño de Software, Universidad de los Andes, 2015-20

#Lo que hay que instalar (utilicen pip):

-Python 2.7
-Django 1.8
-gunicorn
-uWSGI
-gevent

Utilicen pip para instalar, es sencillo. Usen sudo para autenticarse.  

#Para correr la aplicación:

Sobre gunicorn (con archivo de config y workers gevent async):

gunicorn tbcSite.wsgi -c gunicorn.py.ini --worker-class gevent

Sobre uWSGI (con archivo de config):

uwsgi --ini uwsgi.py.ini

#Para no tener problemas de cookies o autenticación al hacer pruebas de carga:

Reemplacen el archivo 'login.html' de Django por el archivo de mismo nombre que está en el folder "recursos_Django" del proyecto. La ruta del archivo de Django en OS es:

/Library/Python/2.7/site-packages/django/contrib/admin/templates/admin/login.html

Reemplacen el archivo 'middleware.py' de Django por el archivo de mismo nombre que está en el folder "recursos_Django" del proyecto. La ruta del archivo de Django en OS es:

/Library/Python/2.7/site-packages/django/contrib/auth/middleware.py

De lo contrario cualquier HTTP request va a devolver la página de login. Una vez reemplacen los archivos van a estar autenticados permanentemente como 'ramirezamayas'.
