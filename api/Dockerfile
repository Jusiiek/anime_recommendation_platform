FROM python:3.10 as build-python

RUN apt-get -y update
COPY ./requirements.txt ./arp_api/

COPY . /arp_api
WORKDIR ./arp_api

RUN pip3 install -r requirements.txt
