# Setting up Apache2 + mod_wsgi + Django on Ubuntu 18.04
2018-12-21

**Apache responds to HTTP requests and either server a static webpage or hand-off specific requests to Python providing the ability to develop dynamic websites.**

## Installing Apache HTTP Server
1. sudo apt update
2. sudo apt install apache2 apache2-dev
3. sudo systemctl status apache2
4. sudo ufw allow 'Apache Full' && sudo ufw status

* Confirm Apache is working by visiting server's address. ex) 192.168.111.200:80
* If 'sudo ufw deny www', you won't be able to connect.
* You can confirm all in-and-out TCP packets by sudo tcpdump -n port 80
* 'Apache Full' opens both HTTP(80) and HTTPS(443) ports.
* Apache Virtual Hosts files are stored in /etc/apache2/sites-available directory. The configuration files found in this directory are not used by Apache unless they are linked to the /etc/apache2/sites-enabled directory.
* To activate a virtual host you need to create a symlink by using the a2ensite command from the configuration files found in the sites-available directory to the sites-enabled directory. To deactivate a virtual host use the a2dissite command.

## Configuring Apache to hand-off certain requests to mod_wsgi, an application handler.
1. sudo cp /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-available/mydomain.com.conf
1. sudo vi /etc/apache2/sites-available/mydomain.com.conf
2. sudo a2ensite mydomain.com.conf && sudo a2dissite 000-default.conf (without specific path)
3. sudo systemctl reload apache2

Add the following line
```
<VirtualHost *:80>
    ...
    WSGIScriptAlias / /var/www/mydomain.com/myapp.wsgi
    Alias "/static" "/var/www/mydomain.com/static/"
</VirtualHost>
```

* If you get an error when you run sudo apache2ctl restart,
    1. sudo vi /etc/apache2/conf-available/servername.conf
    2. Insert the line 'ServerName localhost'
    3. sudo a2enconf servername
    4. sudo systemctl reload apache2 (or sudo apache2ctl restart) (or sudo service apache2 restart)

## Installing libapache2-mod-wsgi-py3 (For Python 3)
1. sudo apt install libapache2-mod-wsgi-py3
2. sudo a2enmod wsgi (Already enabled by default)

## WSGI is a specification that describes how a web server communicates with web applications. Most if not all Python web frameworks are WSGI compliant, including Flask and Django; but to quickly test if you have your Apache configuration correct you’ll write a very basic WSGI application.
1. sudo vi /var/www/html/myapp.wsgi (Despite having the extension .wsgi, these are just Python applications.)

```
def application(environ, start_response):
    status = '200 OK'
    output = 'Hello world!'

    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
```
2. Connect to server(192.168.111.200) to see if it works.

## Flask
1. myapp.wsgi

```
import sys
sys.path.insert(0, '/var/www/myapp')

from application import app as application
```

(Python 2)
2. sudo apt install python-pip
3. sudo pip install virtualenv
4. sudo virtualenv venv
5. source venv/bin/activate
6. pip install -r requirements.txt
7. deactivate

(Python 3)
2. sudo apt install python3.6-venv
3. python3 -m venv venv
4. sudo source venv/bin/activate
5. sudo pip3 install -r requirements.txt
7. deactivate

- a2dismod wsgi
- a2enmod wsgi
- In order to use mod_wsgi daemon mod, pip install mod_wsgi is required but it failed due to the lack of 'apxs'.
To solve this issue,
1. sudo apt install apache2-dev (Install apxs on Ubuntu)
2. (venv) pip install mod_wsgi
3. (venv) mod_wsgi-express start-server (Default port: 8000, sudo ufw allow 8000/tcp required)
4. (venv) mod_wsgi-express start-server pizza/wsgi.py (Default port: 8000)

### Connecting into Apache installation
1. (venv) mod_wsgi-express module-config
```
LoadModule wsgi_module "/home/ubuntu/share/pizza/venv/lib/python3.6/site-packages/mod_wsgi/server/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so"
WSGIPythonHome "/home/ubuntu/share/pizza/venv"
```
These are the directives needed to configure Apache to load the mod_wsgi module and tell mod_wsgi where the Python installation directory or virtual environment was located.

2. sudo vi /etc/apache2/mods-available/wsgi.load
Paste the lines printed by step 1.

3. sudo a2enmod wsgi && sudo systemctl reload apache2

### Another way (Without having installed libapache2-mod-wsgi-py3)
1. (venv) mod_wsgi-express install-module
```
LoadModule wsgi_module "/usr/lib/apache2/modules/mod_wsgi-py36.cpython-36m-x86_64-linux-gnu.so"
WSGIPythonHome "/usr"
```

2. sudo vi /etc/apache2/mods-available/wsgi.load
Paste the lines printed by step 1.

3. sudo a2enmod wsgi && sudo systemctl reload apache2

4. sudo vi /etc/apache2/sites-available/mydomain.com
```
WSGIScriptAlias / /path/to/mysite.com/mysite/wsgi.py
WSGIDaemonProcess mydomain.com python-home=/path/to/venv python-path=/path/to/mydomain.com
WSGIProcessGroup mydomain.com

Alias /robots.txt /path/to/mysite.com/static/robots.txt
Alias /favicon.ico /path/to/mysite.com/static/favicon.ico

Alias /media /path/to/mysite.com/media
Alias /static /path/to/mysite.com/static

<Directory /path/to/mysite.com/static>
Require all granted
</Directory>

<Directory /path/to/mysite.com/media>
Require all granted
</Directory>

WSGIScriptAlias / /path/to/mysite.com/mysite/wsgi.py

<Directory /path/to/mysite.com/mysite>
<Files wsgi.py>
Require all granted
</Files>
</Directory>
```

# ENVIRONMENT VARIABLES (VERY IMPORTANT)
1. sudo vi /etc/config.josn
```
{
    "SECRET_KEY": "secret_key",
    "EMAIL_USER": "",
    "EMAIL_PASS": ""
}
```
2. sudo vi /path/to/mysite.com/myproject/settings.py
```
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

...

SECRET_KEY = config['SECRET_KEY']
```

### apache log
1. /etc/apache2/sites-available/mysite.com.conf
```
    LogLevel info
```
2. /var/log/apache2/access.log

### Watching server logs in real-time
1. tail -f /var/log/apache2/access.log
