FROM python:3.10

WORKDIR /home/whatsapp/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

#RUN apt-get update

COPY ./requirements.txt /home/whatsapp/backend/requirements.txt

RUN pip install -r requirements.txt
