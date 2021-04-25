FROM python:3.9-slim-buster

WORKDIR /web

ADD ./requirments.txt .

RUN pip3 install -r requirments.txt 

ADD . . 

ENV FLASK_APP=webpage.py

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
 
