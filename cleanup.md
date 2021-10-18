## Cleanup 
Stop and delete all running containers
```
docker ps
docker stop [CONTAINER-ID]
docker rm [CONTAINER-ID] [CONTAINER-ID] [CONTAINER-ID] 
```
Delete the images that you have created earlier
```
docker image ls
docker rmi [IMAGE-ID] [IMAGE-ID] [IMAGE-ID]
```

Stop all running containers
```
docker stop $(docker ps -q)
# or
docker stop `docker ps -q`
```

Delete all stopped containers
```
docker rm $(docker ps -a -q)
# or
docker rm `docker ps -a -q`
```

Stop and delete all containers; then remove all images
```
docker stop $(docker ps -aq) && docker rm $(docker-q -aq) && docker rmi -f $(docker images -q)
# or
docker stop `docker ps -aq` && docker rm `docker-q -aq` && docker rmi -f `docker images -q`
```