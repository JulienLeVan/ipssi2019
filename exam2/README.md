# Description

Voici la liste des dossiers contenus dans le dossier **exam2** :

- ex01 du script shell
```
#!/bin/bash

if [ -e $1 ];then
        ls -l $1 >> /tmp/ls.log
        echo "ls ok"
else
        ls -l $1 2>> /tmp/ls_err.log
        echo "ls fail"
fi
```
- ex02 du script shell
- ex03 du script python
- ex04 du script python
- ex05
- ex06
- ex07
- ex08
- ex09
- ex10
- ex11 - Pas réussi, voici les codes :  
DOCKERFILE
```
FROM alpine:3.9
CMD [ "sh" ]
ADD . /path/inside/docker/container

RUN mkdir /out

VOLUME ["/tmp"]


# RUN echo "hello world" > /out/sort_de_docker.txt

# COPY *.txt /c/Users/Julien/AppData/Local/Temp/

# RUN echo "hello world" > /c/Users/Julien/AppData/Local/Temp/
```
lance_docker.sh
```
#!/bin/bash

docker build -t ipssi/ex14:1 .

docker run -i -t ipssi/ex14:1 /bin/sh


```
- ex13
- ex14
- ex15
