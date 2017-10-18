FROM python:3

RUN apt-get update 
RUN apt-get install -y groff-base
RUN apt-get install -y less
RUN apt-get install -y zip

RUN pip install awscli

WORKDIR /usr/src/app
