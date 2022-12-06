FROM python:3.10

WORKDIR /.

COPY . .

RUN pip3 install -r requirements.txt
RUN pip3 uninstall -y ffmpeg-python
RUN pip3 uninstall -y ffmpeg

RUN pip3 install ffmpeg-python
#RUN pip install ffprobe

#RUN apt-get -y update
#RUN apt-get -y upgrade
#RUN apt-get install -y ffmpeg


#COPY . /clipcut

CMD ["python3", "app.py"]