FROM python:3.9

RUN mkdir /app
WORKDIR /app

#----
RUN set -x \
    && add-apt-repository ppa:mc3man/trusty-media \
    && apt-get update \
    && apt-get dist-upgrade \
    && apt-get install -y --no-install-recommends \
        ffmpeg \ #RUN apt-get -y update
#RUN apt-get install -y ffmpeg
#RUN pip3 install ffmpeg-python
#----

COPY requirements.txt ./
RUN pip3 install --no-cache-dir --user -r requirements.txt


#----

#----

COPY . .


ENTRYPOINT ["/usr/bin/python3", "./app.py" ]