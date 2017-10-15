# cat-a-gram
Cat-a-gram the latest craze in web services

## Overview

This is an example of a simple RESTful service with an API call to theCatAPI.  I'm building the application tier image from the ground up to demonstrate the construction of a complete dockerized application.

The foundation from the bottom up is the following:

App Tier:

Redis
Flask
python3.6
centos

DB Tier:

PostgreSQL
centos

## Build Instructions

### App Tier Build Instruction

```
# docker build -t cat-a-gram app/.
``` 

### DB Tier Build instruction

```
# docker build -t cat-a-gram-model db/.
```

## Run Instructions

### App Tier Run Instructions
```
# docker run -e "API_URL=http://thecatapi.com/api/images/get?format=xml&api_key=AbCdEfG" -e "DB_NAME=mydbname" -e "DB_USER=mydbuser" -p 8000:80 cat-a-gram
```

### DB Tier Run Instructions (temporary)
```
# docker run -it -d -e PGSQL_DB_NAME=cg_history -e PGSQL_DB_USERNAME=cat -e PGSQL_DB_USER_PASSWORD=p@ssw0rd -p 5433:5432 cat-a-gram-model
```
