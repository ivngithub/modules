FROM python:3.7

WORKDIR /modules
COPY . /modules
RUN apt-get update && apt-get install telnet
RUN pip install -r requirements.txt