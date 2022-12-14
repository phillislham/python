# so
```js
(<myenv>) 17:39 ~ $ cat /etc/os-release
NAME="Ubuntu"
VERSION="16.04.5 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.5 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
```

# Pasos
## [Youtube Video tutorial by Pretty Printed](https://youtu.be/Y4c4ickks2A)

- Conectate por consola `https://www.pythonanywhere.com/user/<myspace>/consoles/`
- `git clone <your-repo>`
#### my-repo structure:
```js
<your-repo>/
    <your-django-project>/              //django-admin startproject <your-django-project>
        <your-django-base-config>/
            __init__.py
            settings.py
            urls.py
            wsgi.py
        static/
        manage.py
```
- ejecutar `mkvirtualenv --python=/usr/bin/python3.7 <myenv>`
    ```js
    17:33 ~ $ mkvirtualenv --python=/usr/bin/python3.7 <myenv>
    Running virtualenv with interpreter /usr/bin/python3.7
    Using base prefix '/usr'
    /usr/local/lib/python2.7/dist-packages/virtualenv.py:1041: DeprecationWarning: 
    the imp module is deprecated in favour of importlib; 
    see the module's documentation for alternative uses
    import imp
    New python executable in /home/<myspace>/.virtualenvs/<myenv>/bin/python3.7
    Also creating executable in /home/<myspace>/.virtualenvs/<myenv>/bin/python
    Installing setuptools, pip, wheel...done.
    virtualenvwrapper.user_scripts creating /home/<myspace>/.virtualenvs/<myenv>/bin/predeactivate
    virtualenvwrapper.user_scripts creating /home/<myspace>/.virtualenvs/<myenv>/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /home/<myspace>/.virtualenvs/<myenv>/bin/preactivate
    virtualenvwrapper.user_scripts creating /home/<myspace>/.virtualenvs/<myenv>/bin/postactivate
    virtualenvwrapper.user_scripts creating /home/<myspace>/.virtualenvs/<myenv>/bin/get_env_details    
    ```
    - **`the imp module is deprecated in favour of importlib;`**
        - No encontr?? nada para esta advertencia

#### Los paquetes que necesito:
- pip install django
- pip install django-debug-toolbar
- pip install djangorestframework
- pip install django-rest-swagger
- pip install mysqlclient
```js
(venv1) 18:11 ~ $ pip freeze
-f /usr/share/pip-wheels
certifi==2019.3.9
chardet==3.0.4
coreapi==2.3.3
coreschema==0.0.4
Django==2.2.1
django-debug-toolbar==1.11
django-rest-swagger==2.2.0
djangorestframework==3.9.3
Glances==3.1.0
idna==2.8
itypes==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
mysqlclient==1.4.2.post1
openapi-codec==1.3.2
psutil==5.6.2
pytz==2019.1
requests==2.21.0
simplejson==3.16.0
sqlparse==0.3.0
uritemplate==3.0.0
urllib3==1.24.3
```
- Vamos a: `https://www.pythonanywhere.com/user/<myspace>/webapps/#tab_id_<myspace>_pythonanywhere_com`
- En virtualenv configuramos la ruta:
    - `/home/<myspace>/.virtualenvs/<myenv>`
- Editar:
    - `https://www.pythonanywhere.com/user/<myspace>/files/var/www/<myspace>_pythonanywhere_com_wsgi.py?edit`
    - Quitamos todo lo que no sea parte del framework que estamos usando, en este caso Django.
    - configuramos la variable **path**:
        - `/home/<myspace>/<your-repo>/<your-django-project>`
    - configuramos **DJANGO_SETTINGS_MODULE**
        - `<your-django-base-config>.settings`
    - guardamos y cerramos
    ```py
    import os
    import sys

    path = '/home/<myspace>/<your-repo>/<your-django-project>'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = '<your-django-base-config>.settings'
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
    ```
- Vamos a: **settings.py**
    - `ALLOWED_HOSTS = ["<myspace>.pythonanywhere.com"]`
    - configuramos **static**
        - Hay que configurar la variable **STATIC_ROOT**
        - `STATIC_ROOT = '/home/<myspace>/<your-repo>/<your-django-project>/static/'`
        - hay que ejecutar en prod: **`python manage.py collectstatic`**
            - [explicaci??n de este comando](https://stackoverflow.com/questions/34586114/whats-the-point-of-djangos-collectstatic)
            - ![resultado](https://trello-attachments.s3.amazonaws.com/5c8401cf1c6b4163c9b2419b/413x480/38e032a8615fb8ce9727a915d42f3384/image.png)
        - Vamos a: `https://www.pythonanywhere.com/user/<myspace>/webapps/#tab_id_<myspace>_pythonanywhere_com`
        - Secci??n: **Static files:**
            - `url: /static/`
            - `directory: /home/<myspace>/<your-repo>/<your-django-project>/static/`
    - **Reload!...**
    - Funciona!! ^^

## Mysql
- [C??mo hacer un restore](https://help.pythonanywhere.com/pages/MySQLBackupRestore/)
- `mysql -u yourusername -h yourusername.mysql.pythonanywhere-services.com 'yourusername$dbname'  < db-backup.sql`
    - Esto no funciona :S
    - Esto s??:
        ```js
        USE <myspace>$<mydbname>;
        SOURCE /home/<myspace>/prj_python37/apirest/db/<mydbname>_2.0.3.sql;
        ```

## Errores:
- Si ejecuto: `python manage.py runserver` 
    ```js
    File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
    File "<frozen importlib._bootstrap_external>", line 728, in exec_module
    File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
    File "/home/<myspace>/<your-repo>/<your-django-project>/<your-django-base-config>/settings.py", line 1, in <module>
    from .config.dev import *
    File "/home/<myspace>/<your-repo>/<your-django-project>/<your-django-base-config>/config/dev.py", line 1, in <module>
    from .base import *
    File "/home/<myspace>/<your-repo>/<your-django-project>/<your-django-base-config>/config/base.py", line 15, in <module>
    import django_heroku
    ModuleNotFoundError: No module named 'django_heroku'    
    ```
    - Quito las dependencias de heroku y parece que esto tira :)




