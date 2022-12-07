FROM python:3.10

WORKDIR /.

COPY . .

RUN apt-get -y update
RUN apt-get install -y python3-pip
RUN apt-get install -y ffmpeg
RUN pip3 install --user -r requirements.txt

RUN pip3 uninstall -y ffmpeg-python
RUN pip3 uninstall -y ffmpeg

RUN pip3 install python-ffmpeg
#RUN pip install asyncffmpeg

ENTRYPOINT [ "python3" ]

CMD ["./app.py"]