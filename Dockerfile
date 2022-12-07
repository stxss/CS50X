FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt


#----
RUN apt-get -y update
RUN apt-get install -y ffmpeg
#----

COPY . .


ENTRYPOINT ["/usr/bin/python3", "./app.py" ]