# solumovil
solumovil es un servicio que busca mejorar la forma en que se maneja el sistema de transporte público, Universidad de los Andes, 2015-20.

### Instalación
Deben tener virtualenv instalado globalmente:
```sh
$ [sudo] pip install virtualenv
```

Creen un entorno virtual llamado venv, este contendrá las dependencias requeridas para correr el proyecto de manera satisfactoria y evitará inconvenientes con las versiones:
```sh
$ virtualenv venv
```

Asegurense de activar su ambiente virtual siempre que vayan a trabajar:
```sh
$ source venv/bin/activate
```

Pueden verificar que su entorno está activo por el prefijo que les aparecerá en la consola:
```sh
# Antes
$
# Despues
(venv) $
```

Pueden desactivar el ambiente virtual en cualquier momento usando:
```sh
$ deactivate
```

El repositorio contiene un archivo generado por *pip* llamado **requirements.txt**, este contiene las dependencias necesarias para correr el proyecto junto a sus respectivas versiones. Pueden utilizar *pip* para instalar el contenido de este archivo:
```sh
$ pip install -r requirements.txt
```

### Uso

Inicialicen la base de datos *PostgreSQL* (solo la primera vez):
```sh
$ initdb /usr/local/var/postgres
```

En caso de que la inicialización no sea exitosa, borren la carpeta **postgres**:
```sh
$ rm -rf /usr/local/var/postgres
```

Activen la base de datos *PostgreSQL*:
```sh
$ postgres -D /usr/local/var/postgres
```

Instalen *Pgbouncer*
```sh
$ brew install pgbouncer
```

Creen el rol admin
```sh
$ createuser -d admin
```

Creen la base de datos
```sh
$ createdb mydb
``

Activen el balanceador para la base de datos *Pgbouncer*:
```sh
$ pgbouncer pgbouncer.ini
```

Para correr sobre el servidor de desarrollo Django:
```sh
$ python manage.py runserver
```

Para correr sobre *Gunicorn*:
```sh
$ gunicorn -c gunicorn.config.py tbcSite.wsgi
```

### Nuevas dependencias
Recuerden que cada vez que hagan *pull*, deben verificar si hay nuevas dependencias corriendo el archivo **requirements.txt**:
```sh
$ pip install -r requirements.txt
```

En el momento que deban agregar nuevas dependencias con pip, deben actualizar el archivo **requirements.txt**
```sh
$ pip freeze > requirements.txt
```
