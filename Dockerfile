FROM python:2.7
WORKDIR /home/app/

RUN apt-get -y update
RUN apt-get -y install python-dev build-essential
RUN apt-get -y install python-pip
RUN pip install --upgrade pip

ADD requirements.txt .
RUN pip install -r ./requirements.txt
ADD . .

CMD python insert_continuously.py