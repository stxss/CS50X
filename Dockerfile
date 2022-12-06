FROM python:3.10

WORKDIR /.

COPY . .

RUN pip install -r requirements.txt
RUN pip uninstall -y ffmpeg-python
RUN pip install ffmpeg-python
RUN pip install ffprobe

RUN sudo apt update
RUN sudo apt install ffmpeg


#COPY . /clipcut

CMD ["python3", "app.py"]

