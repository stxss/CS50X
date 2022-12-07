FROM python:3.9

RUN mkdir /app
WORKDIR /app

#----
RUN apt-get -y update
RUN apt-get install -y ffmpeg
#----


COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt


#----
RUN pip3 uninstall -y ffmpeg-python
RUN pip3 uninstall -y ffmpeg
RUN pip3 install ffmpeg-python
#----

COPY . .


ENTRYPOINT ["/usr/bin/python3", "./app.py" ]