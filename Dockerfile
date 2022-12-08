FROM python:3.9


#----
EXPOSE 80
#----

RUN mkdir /app
WORKDIR /app

#----
#COPY --from=jrottenberg/ffmpeg /usr/local ./
#----


#----
#RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg
RUN apt-get -y update
RUN apt-get install -y ffmpeg
#RUN pip3 install ffmpeg-python
#----

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt


#----
RUN pip3 install --no-cache-dir ffmpeg-python
#----

COPY . .

ENTRYPOINT ["/usr/bin/python3", "./app.py" ]
