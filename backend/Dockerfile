FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install curl -y
RUN apt-get install python3.8 -y
RUN apt-get install python3-pip -y
RUN pip3 install --upgrade pip

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt


COPY ./api /app

CMD python3 main.py