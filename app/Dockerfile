# cat-a-gram
# by: Christopher Landry
# date: 13-Oct-2017
#
# VERSION	0.0.1

# Start from a base Linux OS
FROM centos:latest

# Update latest patches
RUN yum update -y

# Install gcc
RUN yum install gcc -y
RUN yum install gcc-c++ -y
RUN yum install make -y
RUN yum install zlib-devel -y
RUN yum install openssl-devel -y
RUN yum install wget -y

# Install Python 3.6
WORKDIR /usr/src
RUN wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tgz
RUN tar -zxf Python-3.6.1.tgz
WORKDIR /usr/src/Python-3.6.1
RUN ./configure
RUN make altinstall
WORKDIR /usr/local

# Set the app working dir
WORKDIR /app

# Copy Src Files
COPY app.py /app/app.py
COPY model/__init__.py /app/model/__init__.py
COPY model/cats.py /app/model/cats.py
COPY service/__init__.py /app/service/__init__.py
COPY service/api.py /app/service/api.py
COPY requirements.txt /app/requirements.txt

# Install the Application Requirements
RUN pip3.6 install -r /app/requirements.txt

CMD ["python3.6","/app/app.py"]
