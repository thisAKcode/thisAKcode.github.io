title: Setup a Docker container
date: 2023-05-22 12:00
author: Alex

### Short Notes on Docker

Before you dive deep you need to figure out whether you need a Docker container and how it would be useful in your project.
To figure out how docker would be useful this Fireship video might be good place to start: <https://www.youtube.com/watch?v=Gjnup-PuquQ>.

### Docker nomenclature


An image : hard drive for virtual machine. Start up with base image. Image is a structure having plenty of parameters but it is not an execution of a container. Docker image - a private file system just for your container. It provides all the files and code your container needs.

A container: Is instance where you run an image almost like virtual machine. Example: you run uWSGI to serve up web content. Only thing you run in the container is uWSGI. Start a container based on the image you built in the previous step. Running a container launches your application with private resources, securely isolated from the rest of your machine.

A volume: Container is stateless meaning its content disappears. Map folders inside of the container to real folders on the host. Changes to particular folder (also called volume) will stay across executions of the containers. They are persistent.  

The ports: Like the file system is isolated so is the networking around these containers. Containers can talk out to the network but can't listen on a port(not exposed). In web server | db situation you need to connect. Need to expose some ports. 

The entry points: When I run container entry point into container is a procedure pointed at your app files, config, etc. 

Dockerfile: Way we build an image is to create a dockerfile. Dockerfile - series of commands to execute on Linux machine starting from the base image to obtain the configured image. All commands apt install things are copy config file etc. are put into a Docker file and all these commands are layered. 


### Set up Docker container

First time I struggled with enable docker wich was resolved by turning on windows features.
 
#### Clone 
I executed this command as per Docker quickstart tutorial:
`docker run --name repo alpine/git clone https://github.com/docker/getting-started.git docker cp repo:/git/getting-started/ .`
It created the folder here: `C:\Users\Aleks\getting-started `

#### Build the Image 
 Look at the definition at the top.
 To create one `cd C:\Users\Aleks\getting-started`. 
 ```bash
 cd getting-started
 docker build -t docker101tutorial .
 ```
 
### Run Your First Container
Start a container based on the image you built in the previous step. Running a container launches your application with private resources, securely isolated from the rest of your machine.
```bash
docker run -d -p 80:80 --name docker-tutorial docker101tutorial
```
You'll notice a few flags being used. Here's some more info on them:

    -d - run the container in detached mode (in the background)
    -p 80:80 - map port 80 of the host to port 80 in the container
    docker101tutorial - the image to use

#### Save and Share Your Image
Save and share requires you:
1. Being owner of Docker ID (create at hub.docker.com) 
2. Once you have Docker ID make sure you signed in to Docker Hub. 

Benifits of sharing: 
Other users can easily download and run the image on any destination machine.

Sharing instructions:
```
docker tag docker101tutorial alekseikupiakov1docker1user/docker101tutorial
docker push alekseikupiakov1docker1user/docker101tutorial
```
After that you can see what you've saved on [Hub](https://hub.docker.com/repository/docker/alekseikupiakov1docker1user/docker101tutorial)


### This is how you would run a Docker container
Once Docker installed you can try to run:
```shell
# all the processes
docker ps               
# all docker images 
docker images
```
If everything runs then you can  your first container:
`docker run ubuntu:latest` or docker run ubuntu:18.04
This downloads ubuntu latest first. once done you can try to run it again and you will see that it run a short while then it shuts down. 

`docker run -it ubuntu:latest bash ` interactive mode.
Then test to check `hostname`, `ls`, and `ps` of your image:
```bash
 λ  docker run -it ubuntu:latest bash
root@2fe6d723b3d7:/# ls
bin   dev  home  lib32  libx32  mnt  proc  run   srv  tmp  var
boot  etc  lib   lib64  media   opt  root  sbin  sys  usr
root@2fe6d723b3d7:/# hostname
2fe6d723b3d7
root@2fe6d723b3d7:/# ps
  PID TTY          TIME CMD
    1 pts/0    00:00:00 bash
   12 pts/0    00:00:00 ps
root@2fe6d723b3d7:/#exit
``` 
As you saw for now you just run bash.

```bash 
docker ps -a
CONTAINER ID   IMAGE           COMMAND       CREATED         STATUS                          PORTS     NAMES
2fe6d723b3d7   ubuntu:latest   "bash"        6 minutes ago   Exited (0) About a minute ago             zen_rubin
4ec825b2520c   ubuntu:latest   "/bin/bash"   7 minutes ago   Exited (0) 7 minutes ago                  charming_dijkstra
22d88344ccd1   ubuntu:latest   "-v"          7 minutes ago   Created                                   magical_stonebraker
400667abc080   ubuntu:latest   "-v"          8 minutes ago   Created                                   stoic_wu
b583732ec820   ubuntu:latest   "/bin/bash"   9 minutes ago   Exited (0) 9 minutes ago                  upbeat_allen
```
Things you might want to pay attention  are CONTAINER ID and otherwise funky NAMES. You can reference your container by using either id or name.



### Cheat Sheet 
```
docker -v
docker pull postgres:alpine
docker run --name fastapi-postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine
docker ps
```
```
docker exec -it fastapi-postgres bash
```
```
psql -U postgres
```
```
create database python_db;
create user postgres with encrypted password 'ljlkd%fFDFw12?Dg0vRiF';
 grant all privileges on database python_db to postgres_v2;
\c python_db;
 psql -h localhost -p 5432 postgres;

 \dt
```

ctrl d to quit

### Sources 
Instructions to install docker on [ubuntu](https://docs.docker.com/engine/install/ubuntu/).
