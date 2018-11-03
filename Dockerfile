FROM ubuntu:16.04
ADD . /app
RUN apt-get update
RUN apt-get install -y python3.5 python3-pip
RUN pip3 install -r /app/requirements.txt
EXPOSE 8000
VOLUME /app
USER nobody
WORKDIR /app
CMD gunicorn --bind 0.0.0.0 --workers 5 askme.wsgi
