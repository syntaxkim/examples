# How to install and use docker on Ubuntu 18.04
2019-01-15

[Tutorial][https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04]

## Installing Docker (from official Docker repository)
### Install prerequisite packages which let apt use packages over HTTPS.
1. sudo apt update
2. sudo apt install apt-transport-https ca-certificates curl software-properties-common
### Add the GPT key for the official Docker repository to your system.
3. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
### Add the Docker repository to APT sources
4. sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
### Update the package database with the Docker packages from the newly added repo
5. sudo apt udpate
### Make sure you ar about to install from the Docker repo instead of the default Ubuntu repo
6. apt-cache policy docker-ce
### Finally, install Docker
7. sudo apt install docker-ce
8. sudo systemctl status docker
### Add your username to docker group to avoid typing sudo (Optional)
10. sudo usermod -aG docker ${USER}

## Working with Docker Images
### Docker command
* docker (option) (command) (arguments)
### Check
1. docker run hello-world
(Download hell-world image from Docker Hub which is the default repository, run it)
### Return a list of all images that matches the search string (ubuntu) from Docker Hub.
2. docker search ubuntu
### Donload the official ubuntu image.
3. docker pull ubuntu
### Display the images that have been downloaded.
4. docker images

## Running a Docker Container
### Run a container using the latest image of Ubuntu.
1. docker run -it ubuntu (-it: interactive shell access into the container)
(user)@(container ID)
root@e614215ad046:/#
2. /# apt update (Update the package database inside the container)
3. /# exit (Exit the container)

## Managing Docker Containers
1. docker ps (View the active containers)
2. docker ps -a (View all containers)
3. docker ps -l (View the latest container)
4. docker start e614215ad046 (Start a stopped container)
5. docker stop [id or container name] (Stop a running container)
6. docker rm [id or container name] (Remove a container)
7. docker run --help (For more information)

## Committing Changes in a Container to a Docker Image
Containers can be turned into images which you can use to build new containers.
1. docker commit -m "message" -a "Author Name" container_id repository/new_image_name
(ex: docker commit -m "added Node.js" -a "sammy" d9b100f2f636 sammy/ubuntu-nodejs)
2. docker images

## Pushing Docker Images to a Docker Repository
1. docker login -u docker-registry-username
2. docker push docker-registry-username/docker-image-name
(ex: docker push sammy/ubuntu-nodejs)

## Difference between 'run' and 'start'
* docker run image (Create a new container of an image and execute the container)
* docker start container (Start a stopped container)
