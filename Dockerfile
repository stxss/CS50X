FROM python:3.9

RUN mkdir /app
WORKDIR /app

#----
RUN apt-get -y update
RUN apt-get install -y ffmpeg
#RUN pip3 install ffmpeg-python
#----

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt


#----
RUN pip uninstall ffmpeg-python
RUN pip uninstall ffmpeg

RUN pip install ffmpeg-python
#----

COPY . .


ENTRYPOINT ["/usr/bin/python3", "./app.py" ]