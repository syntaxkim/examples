# Docker Compose with Nginx, Django, Gunicorn, PostgreSQL
2019-01-24

[source](http://pawamoy.github.io/2018/02/01/docker-compose-django-postgres-nginx.html)

### Creating a Django Project
1. django-admin startproject whatever
2. cd whatever
3. gunicorn --bind :8000 whatever.wsgi:application

### Creating a Docker Image
1. vi Dockerfile
```
# Start from an official Python image
FROM python:3.6

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
# RUN pip install -r requirements.txt
RUN pip install django gunicorn

# Copy project files
COPY . /usr/src/app

# Expose the port 8000
EXPOSE 8000

# Define the default command to run when starting the container
CMD gunicorn --bind :8000 whatever.wsgi:application
```
2. docker build . -t whatever
3. docker run -it -p 8000:8000 whatever
* For interactive processes (like a shell), you must use `-i -t` together in order to allocate a tty for the container process.
* `-i -t` is often written `-it`.

### Using docker-compose to add containers for Nginx, PostgreSQL
1. vi docker-compose.yml
```
version: '3'

services:
        djangoapp:
                build: . # Build an image by finding the Dockerfile in this directory.
                volumes:
                        - .:/usr/src/app
                ports:
                        - 8000:8000
                depends_on:
                        - nginx
                        - db1

        nginx:
                image: nginx:latest
                ports:
                        - 8000:80
                volumes:
                        - ./config/nginx/conf.d:/etc/nginx/conf.d
                depends_on:
                        - djangoapp # Wait for djangoapp to be ready before starting this service.

        db1: # This key name must be the same as in DATABASES settings in Django.
                image: postgres:10
                env_file:
                        - config/db/db1_env
                networks:
                        - db1_network
                volumes:
                        - db1:/var/lib/postgresql/data

networks:
        nginx_network:
                drvier: brdige
        db1_network:
                driver: bridge

volumes:
        db1_volume:
        static_volume:
        media_volume:
```