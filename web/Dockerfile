FROM python:3.8

WORKDIR /web

ADD ./requirments.txt .

RUN pip3 install -r requirments.txt 

ADD . . 

ENV FLASK_APP=webpage.py

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
 
