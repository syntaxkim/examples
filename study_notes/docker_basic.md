# Docker - Understanding Basic Concepts
2019-01-23

[Tutorial Video](https://www.youtube.com/watch?v=VzzwnsLX_5o)

## Creating an Ubuntu image
1. mkdir twitch
2. cd twitch
3. vi Dockerfile
```
FROM ubuntu:18.04
```
4. docker ps
```
(No container is running)
```
5. docker build -t image_name:tag . (Build an image from Dockerfile in currenct directory)
* `--tag , -t`: name and optionally a tag in the 'name:tag'format
```
Sending build context to Docker daemon  2.048kB
Step 1/1 : FROM ubuntu:18.04
18.04: Pulling from library/ubuntu
38e2e6cd5626: Pull complete
705054bc3f5b: Pull complete
c7051e069564: Pull complete
7308e914506c: Pull complete
Digest: sha256:7a4bd65e1457b8a85d3efa2b3404c78e96f18978b8db3bbe0ce24b8d0e7dd629
Status: Downloaded newer image for ubuntu:18.04
 ---> 20bb25d32758
Successfully built 20bb25d32758 (image_id)
```
6. docker run -it image_id/image_name
7. root@28e4d9f10505:/# uname
```
Linux
```
8. root@28e4d9f10505:/# exit

## Mounting current directory to docker's /mnt directory
1. pwd
```
/home/ubuntu/twitch
```
2. docker run -v /home/ubuntu/twitch:/mnt -it image_id (or, docker run -v ${PWD}:/mnt -it image_id)
3. root@28e4d9f10505:/# ls /mnt
```
Dockerfile
```
4. root@28e4d9f10505:/# apt update
5. root@28e4d9f10505:/# apt install vim
7. root@28e4d9f10505:/# vim (Vim editor is running)
8. root@28e4d9f10505:/# exit
9. docker run -v /home/ubuntu/twitch:/mnt -it image_id (Rerun a docker image)
10. root@28e4d9f10505:/# vim
```
bash: vim: command not found
```
* Docker image is desinged to be extremely lightweight - not even include vim.
* All the changes made to the image are `ephemeral`.

## Creating an additional layer
1. vi Dockerfile
```
FROM ubuntu:18.04

RUN apt update
RUN apt install -y vim
```
* `RUN apt update && install -y vim` is also valid.
* You should not need to use `apt update` unless any third-party software is needed.
2. docker build .
```
Processing triggers for libc-bin (2.27-3ubuntu1) ...
Removing intermediate container c9b025f71637
 ---> b400763d9992
Successfully built b400763d9992 (image_id)
```
3. docker run -v ${PWD}:/mnt -it image_id
4. root@28e4d9f10505:/# vim
* Vim editor is now working because it's pre-installed during building the image.
5. docker build . (Try building an image again)
```
Sending build context to Docker daemon  2.048kB
Step 1/3 : FROM ubuntu:18.04
 ---> 20bb25d32758
Step 2/3 : RUN apt update
 ---> Using cache
 ---> 20fd91a7982f
Step 3/3 : RUN apt install -y vim
 ---> Using cache
 ---> b400763d9992
Successfully built b400763d9992
```
* Docker uses the built images so it does not have to install from the bottom.
* By default, if you don't specify a command, the Docker container spawns `bash`.
* To overwrite that, add `CMD apt install -y foo && bash` into the Dockerfile.