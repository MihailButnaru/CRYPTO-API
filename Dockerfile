FROM python:latest
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
# All the aditional env variable must be added, check the env.sample
ENV PYTHONUNBUFFERED 1

RUN mkdir /crypto_service

RUN apt-get -y update
RUN apt-get install -y python python-pip python-dev python-psycopg2 postgresql-client 

ADD requirements.txt /crypto_service/requirements.txt
RUN pip install -r /crypto_service/requirements.txt

RUN apt-get -y update && apt-get -y autoremove
WORKDIR /crypto_service

EXPOSE 8000

CMD gunicorn -b :8000 crypto_service.core.wsgi