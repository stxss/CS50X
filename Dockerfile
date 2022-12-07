FROM python:3.10

ENV PYTHONPATH "${PYTHONPATH}:/."

WORKDIR /.

COPY . .

RUN apt-get -y update
RUN apt-get install -y python3-pip
RUN apt-get install -y ffmpeg
RUN pip3 install --user -r requirements.txt

RUN pip3 uninstall -y ffmpeg-python
RUN pip3 uninstall -y ffmpeg

#RUN pip3 install ffmpeg-python
RUN pip3 install python-ffmpeg
RUN pip install asyncffmpeg
#RUN pip install ffprobe


#RUN apt-get -y upgrade
#RUN apt-get install -y ffmpeg

CMD ["python3 app.py"]