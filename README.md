# cat-a-gram
Cat-a-gram the latest craze in web services

## Overview

This is an example of a simple RESTful service with an API call to theCatAPI.  I build the application tier and data tier image from the ground up to demonstrate the construction of a complete dockerized application.

The foundation from the bottom up is the following:

App Tier:

Flask
python3.6
centos

DB Tier:

PostgreSQL
centos

## Build Instructions

### Build Docker Composer File

```
# ./configure
```

This will ask you for your Database name, DB Username and Password and construct the Docker Compose file. 

### App Tier Build Instruction

```
# docker build -t cat-a-gram app/.
``` 

or

```
# make cat-a-gram
```

### DB Tier Build instruction

```
# docker build -t cat-a-gram-model db/.
```

or

```
# make cat-a-gram-model
```

## Run Instructions

```
# docker-compose up -d
```
