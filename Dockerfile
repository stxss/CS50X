FROM python:3.9

RUN mkdir /app
WORKDIR /app

#----
ENV FFMPEG_VERSION=4.3.2
RUN apt-get -y update
RUN apt-get install -y ffmpeg
#RUN pip3 install ffmpeg-python
#----

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt


#----

#----

COPY . .


ENTRYPOINT ["/usr/bin/python3", "./app.py" ]