FROM python:3.9

#----
EXPOSE 80
#----

RUN mkdir /app
WORKDIR /app

#----
RUN apt-get -y update
RUN apt-get install -y ffmpeg
#----

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt

#----
RUN pip3 install --no-cache-dir ffmpeg-python
RUN pip3 install --no-cache-dir deepgram-sdk
#----

COPY . .

#ENTRYPOINT ["/usr/bin/python3", "app.py" ]
ENTRYPOINT ["/usr/local/bin/python", "app.py" ]
