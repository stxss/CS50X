FROM python:3.10

WORKDIR /.

COPY . .

RUN pip install -r requirements.txt
RUN pip uninstall ffmpeg
RUN pip install ffmpeg-python


#COPY . /clipcut

CMD ["python3", "app.py"]

