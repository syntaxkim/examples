# Setting up Nginx + Guniorn + Django on Ubuntu 18.04
2018-12-22

[Tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04)

## Overall data flow
HTTP request > nginx > gunicorn.socket > gunicorn.service > wsgi:application

## Set up nginx.
1. sudo apt update
2. sudo apt install nginx
3. sudo systemctl status nginx
4. sudo ufw allow 'Nginx Full' && sudo ufw status

## Setting Up Server Blocks (Recommended)
You may want to use server blocks to encapsulate configuration details and host multiple domains.
1. sudo cp -r path/to/mydomain.com /var/www/mydomain.com
2. sudo chown -R $USER:$USER /var/www/mydomain.com
3. sudo chmod -R 755 /var/www/example.com

## Configuration (Best practices)
1. sudo rm /etc/nginx/sites-enabled/default (optional)
2. touch /etc/nginx/sites-available/mydomain.com.conf
3. sudo ln -s /etc/nginx/sites-available/mydomain.com.conf /etc/nginx/sites-enabled/mydomain.com.conf
* Unlike Apache which uses a2ensite and a2dissite to link configuration files, nginx uses just 'ln'.
ln (symbolic link)
-s (soft link, if not used, hard link between two files)
/etc/nginx/sites-available/mydomain.com.conf (base file)
/etc/nginx/sites-enabled/mydomain.com.conf (link)

4. sudo vi /etc/nginx/sites-enabled/mydomain.com.conf
```
# Virtual Host configuration for mydomain.com

server {
    listen 80;
    listen [::]:80; # IPv6
    server_name mydomain.com;
    access_log /var/log/nginx/mydomain.log; # Log access on a different log file-acces.log

    location / static {
        alias /var/www/mydomain.com/static;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
* Nginx is set up as a reverse proxy server to a Gunicorn server running on localhost port 8000.

5. sudo systemctl reload nginx

## Manage Nginx Service.
* sudo systemctl stop nginx
* sudo systemctl start nginx
* sudo systemctl restart nginx
* sudo systemctl reload nginx (After making configuration changes)
* sudo systemctl disable nginx (Do not start on boot.)
* sudo systemctl enable nginx 


# gunicorn (Debian GNU/Linux)
There are two ways to install gunicorn - either using system package or virtualenv.
Using system package is more recommended as it provides improved security.

## Using system package (apt)

### Install gunicorn
1. sudo apt install gunicorn
2. sudo apt update


## Using virtualenv (Use the latest version)
### Set up python virtualenv (Refer to ubuntu_venv.md)
### Install gunicorn
1. (venv) pip install gunicorn
2. (venv) pip install greenlet eventlet (for async workers)
### Run gunicorn.
1. gunicorn application:app (Flask)
2. gunicorn (project_name).wsgi (Django) --workers=3 (Run on http://127.0.0.1:8000 by default) --daemon (Run on background)
* The recommended number of workers to start off with: (2 x $num_cores) + 1
3. kill (gunicorn's process number)

### If not using nginx, (For test purpose)
2. gunicorn (project_name).wsgi --bind(or -b) 0.0.0.0:8000 (bind with 0.0.0.0:8000)

# Connect to server to test the app.
* No need to specify port number in the URL, nginx takes care of port numbers - it's a proxy server.

# Systemd
### Creating systemd Socket and Service Files for Gunicorn
The Gunicorn socket will be created at boot and will listen for connections.
When a connection occurs, systemd will automatically start the Gunicorn process to handle the connection.

1. sudo vi /etc/systemd/system/gunicorn.socket
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Only start this service after the networking target has been reached.
2. sudo vi /etc/systemd/system/gunicorn.service
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
# PIDFile=/run/gunicorn/pid
User=ubuntu
Group=www-data
# RuntimeDirectory=gunicorn
WorkingDirectory=/var/www/mydomain.com
ExecStart=/var/www/mydomain.com/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          appname.wsgi:application
# ExecReload=/bin/kill -s HUP $MAINPID
# ExecStop=/bin/kill -s TERM $MAINPID
# PrivateTmp=true

[Install]
WantedBy=multi-user.target

```

3. sudo systemctl daemon-reload
4. sudo systemctl start gunicorn.socket
5. sudo systemctl enable gunicorn.socket
6. file /run/gunicorn.sock (Check for the existence of the gunicorn.sock file within /run)
/run/gunicorn.sock: socket
7. sudo journalctl -u gunicorn.socket (Check the Gunicorn socket's logs)
8. sudo systemctl status gunicorn (Check status)

Include the standard proxy_params file included with the Nginx installation.
9. sudo vi /etc/nginx/sites-available/mysite.com
```
server {
        listen 80;
        listen [::]:80;
        server_name mydomain.com;
        access_log /var/log/nginx/mydomain.log;

        location = /favicon.ico { access_log off; log_not_found off; }

        location /static {
                alias /var/www/pizza.com/static;
        }
        location / {
                include proxy_params;
                # proxy_pass http://127.0.0.1:8000;
                proxy_pass http://unix:/run/gunicorn.sock;
                # proxy_set_header Host $host;
                # proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
}
```

10. sudo nginx -t (Test Nginx configuration for syntax errors)
11. sudo ufw delete allow 8000 (No long need access to the development server)
12. sudo ufw allow 'Nginx Full'

# The primary place to look for more information
* sudo tail -F /var/log/nginx/error.log
* sudo tail -f /var/log/nginx/error.log

# Permission error
* namei -l /run/gunicorn.sock
f: /run/gunicorn.sock
drwxr-xr-x root root /
drwxr-xr-x root root run
srw-rw-rw- root root gunicorn.sock
(Desired output)

# Further troubleshooting
* sudo journalctl -u nginx (Nginx process logs)
* sudo less /var/log/nginx/access.log (Nginx access logs)
* sudo less /var/log/nginx/error.log (Nginx error logs)
* sudo journalctl -u gunicorn (Gunicorn application logs)
* sudo journalctl -u gunicorn.socket (Gunicorn socket logs)

# Update configuration or application
* sudo systemctl restart gunicorn (Update Django application)
* sudo systemctl daemon-reload
* sudo systemctl restart gunicorn.socket gunicorn.service (Update Gunicorn socket or service files)
* sudo nginx -t && sudo systemctl restart nginx (Update Nginx server block configuration)
