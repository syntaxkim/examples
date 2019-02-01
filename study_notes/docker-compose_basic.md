# Using docker-compose 
2019-01-15

**docker-compose is a tool for defining and running multi-container Docker applications.**
The most common use cases are
- Development environments
- Automated testing environments
- Single host deployments

### Prerequsites (other than Docker)
* sudo apt install docker-compose (ubuntu)

### Example Application
1. mkdir hello
2. cd hello
3. sudo vi application.py
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

### Define your app’s environment with a Dockerfile
4. sudo vi Dockerfile
```
FROM python:3
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app
RUN pip install -r requirements.txt
ADD . /usr/src/app
```

### Define the services that make up your app in docker-compose.yml
5. sudo vi docker-compose.yml
```
version: '3'

services:
        web:
                build: .
                command: python3 application.py
                volumes:
                        - .:/usr/src/app
                ports:
                        - "5000:5000"
```

### Compose starts and runs your entire app
6. docker-compose up
* It will look for docker-compose.yml and create two images-python, hello-web.
* And then start the container.
7. sudo ufw allow 5000 (if port is not open)
8. (ip_address):5000
9. docker start container_id
