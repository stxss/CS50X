FROM python:3.9




RUN mkdir /app
WORKDIR /app

#----
#COPY --from=mwader/static-ffmpeg:4.1.4-2 /ffmpeg /ffprobe /usr/local/bin/

#jrottenberg version
ENV LD_LIBRARY_PATH=/usr/local/lib
COPY --from=jrottenberg/ffmpeg /usr/local ./
#----


#----
RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg
#RUN apt-get -y update
#RUN apt-get install -y ffmpeg
#RUN pip3 install ffmpeg-python
#----

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt


#----

#----

COPY . .


ENTRYPOINT ["/usr/bin/python3", "./app.py" ]