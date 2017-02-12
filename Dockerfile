FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python3 python3-pip nodejs npm git
RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN pip3 install --upgrade pip && pip install gunicorn

ADD ./mrr_website /app/mrr_website
ADD ./requirements /app/requirements
ADD requirements.txt /app
ADD autoapp.py /app
ADD bower.json /app
ADD .bowerrc /app

WORKDIR /app


RUN pip3 install -r requirements.txt

RUN npm install -g bower
RUN bower --allow-root install
  
CMD ["gunicorn", "-w4", "-b 0.0.0.0:8080", "autoapp:app"]