# Setting up Nginx + uwsgi + Flask on Ubuntu 18.04
2019-01-19

[Tutorial](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)

## Installing the Components from th Ubuntu Repositories
1. sudo apt update
2. sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

## Creating a Python Virtual Environment
1. sudo apt install python3-venv
2. cd /var/www/mydomain.com
3. python3 -m venv mydomainenv
4. source /var/www/mydomain.com/mydomainenv/bin/activate
5. (mydomainenv) pip install -r requirements.txt
6. (mydomainenv) pip install uwsgi
### Test on test server
1. sudo ufw allow 5000
2. (mydomainenv) python3 application.py
3. http://your_server_ip:5000
### Creating the WSGI Entry Point
1. (mydomainenv) sudo vi wsgi.py
```
from application import app

if __name__ == "__main__":
    app.run()
```

## Configuring uWSGI
1. uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
-s|--socket: bind to the specified UNIX/TCP socket using default protocol
--protocol: force the specified protocol for default sockets
-w|--module: load a WSGI module
2. http://your_server_ip:5000

## Creating a uWSGI Configuration File
1. sudo vi /var/www/mydomain.com/mydomain.ini
```
# [uwsgi] is a header which uWSGI knows to apply the sttings.
[uwsgi]
# wsgi is a module, app is a callable
module = wsgi:app

# Tell uWSGI to set up in master mode.
master = true
# Spawn 5 worker proesses to server requests.
processes = 5

# Call the UNIX socket. (Using socket is more faster and secure)
socket = mydomain.sock
# Change the permissions on the socket so that Nginx can read and write to it.
chmod-socket = 660
# Clean up the socket when the process stops.
vacuum = true

# Ensure that the init system and uWSGI have the same assumptions about what each process signal means.
die-on-term = true

# uwsgi loads environment variables using env argument.
env = SECRET_KEY=VALUE1
env = API_KEY=VALUE2
```
* By default, uWSGI speaks using the `uwsgi` protocol, a fast binary protocol designed to communicate with other servers. Nginx can speack this protocol natively, so it's better to use this than to force communication by HTTP.

## Creating a systemd Unit File
1. sudo vi /etc/systemd/system/mydomain.service
```
[Unit]
Description=uWSGI instance to serve mydomain.com
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/mydomain.com
Environment="PATH=/var/www/mydomain.com/mydomainenv/bin"
ExecStart=/var/www/mydomain.com/mydomainenv/bin/uwsgi --ini mydomain.ini

[Install]
WantedBy=multi-user.target
```
* Creating a systemd unit file allows Ubuntu's init system to automatically start uWSGI and serve the Flask application whenever the server boots.

2. sudo systemctl start mydomain
3. sudo systemctl enable mydomain
* Make sure to enable service or you will get a 502 Bad Gateway Error (Nginx was unable to find mydomain.sock)
4. sudo systemctl status mydomain

## Configuring Nginx to Proxy Requests
1. sudo vi /etc/nginx/sites-available/mydomain
```
server {
        listen 80;
        listen [::]:80;
        server_name mydomain.com;
        access_log /var/log/nginx/mydomain.log;
        error_log /var/log/nginx/mydomain.error.log;

        location = /favicon.ico { access_log off; log_not_found off; }

        location /static {
                alias /var/www/mydomain.com/static;
        }
        location / {
                include uwsgi_params;
                uwsgi_pass unix:/var/www/mydomain.com/mydomain.sock;
        }
}
```

2. sudo ln -s /etc/nginx/sites-available/mydomain /etc/nginx/sites-enabled
3. sudo nginx -t
4. sudo systemctl restart nginx
5. sudo ufw delete allow 5000
6. sudo ufw allow 'Nginx Full'

## Troubleshooting
* sudo less /var/log/nginx/error.log (Nginx error logs)
* sudo less /var/log/nginx/access.log (Nginx access logs)
* sudo journalctl -u nginx (Nginx process logs)
* sudo journalctl -u mydomain (Flask app's uWSGI logs)
* sudo vi application.py
except Exception as err:
    return str(err)

## The latest version of psycopg2 causes OperationalError.
To get around this issue, you need to have source-only installation.
* (virtualenv) pip install psycopg=2.7.4 --no-binary :all:
