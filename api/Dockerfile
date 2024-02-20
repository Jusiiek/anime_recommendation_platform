FROM python:3.10 as build-python

RUN apt-get -y update \
    && apt-get install -y gettext \
    # Cleanup apt cache
    && apt-get clean \
COPY ./requirements.txt ./arp_api/

COPY . /arp_api
WORKDIR ./arp_api

RUN mkdir -p /media /static

RUN python3 -m pip uninstall -y psycopg2
RUN python3 -m pip install psycopg2

RUN pip3 install -r requirements.txt
