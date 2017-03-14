FROM python:3.5.3-alpine

RUN pip install docker-py==1.6.0 boto==2.42.0

ADD watch.py watch.py

CMD [ "python", "./watch.py" ]
