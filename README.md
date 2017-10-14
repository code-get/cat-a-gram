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

## Build Instructions

```
# docker build -t cat-a-gram .
``` 

## Run Instructions

```
# docker run -p 8000:80 cat-a-gram -e API_KEY=AbCdEfG
```
