# Docker Tutorial
2018-11-15

### docker basic commands
- docker build -t friendlyhello .  # Create image using this directory's Dockerfile
- docker run -p 4000:80 friendlyhello  # Run "friendlyname" mapping port 4000 to 80
- docker run -d -p 4000:80 friendlyhello         # Same thing, but in detached mode
- docker container ls                                # List all running containers
- docker container ls -a             # List all containers, even those not running
- docker container stop <hash>           # Gracefully stop the specified container
- docker container kill <hash>         # Force shutdown of the specified container
- docker container rm <hash>        # Remove specified container from this machine
- docker container rm $(docker container ls -a -q)         # Remove all containers
- docker image ls -a                             # List all images on this machine
- docker image rm <image id>            # Remove specified image from this machine
- docker image rm $(docker image ls -a -q)   # Remove all images from this machine
- docker login             # Log in this CLI session using your Docker credentials
- docker tag <image> username/repository:tag  # Tag <image> for upload to registry
- docker push username/repository:tag            # Upload tagged image to registry
- docker run username/repository:tag                   # Run image from a registry

### docker run
* -a=[] : Attach to `STDIN`, `STDOUT` and/or `STDERR`
* -t    : Allocate a pseudo-tty
* -i    : Keep STDIN open even if not attached

### Example
1. Create a file 'application.py'
```
(some Flask source code)
```
2. Create a file 'requirements.txt'
```
Flask
```
3. Create a 'Dockerfile'
```
FROM python:3
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENV HOST su
CMD ["python", "application.py"]
```
4. docker build -t <app_name> .
5. To see where the build image is, docker image ls
6. To run the app, docker run -p 4000:80 <app_name>
7. To run the app in the background (in detached mode), docker run -d 0p 4000:80 <app_name>
8. curl http://localhost:4000
9. To see container ID, docker container ls -a
10. docker container stop <container_id>
11. docker rm <container_id>
12. docker rmi <image_id>
13. docker exec -it <container_id> bash -l
