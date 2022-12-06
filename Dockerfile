FROM python:3.10

WORKDIR /.

COPY . .

#RUN pip install -r requirements.txt
#RUN apt-get install -y ffmpeg
RUN pip install -r requirements.txt
RUN pip uninstall -y ffmpeg-python==0.2.0
RUN pip install ffmpeg-python==0.2.0


#COPY . /clipcut

CMD ["python3", "app.py"]

