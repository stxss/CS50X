FROM python:3.10

COPY "E:\CS50X\."

ADD app.py .

RUN pip install deepgram-sdk
RUN pip install Pyrogram
RUN pip install pyromod
RUN pip install ffmpeg-python
RUN pip install schedule
RUN pip install python-dotenv
RUN pip install TgCrypto

CMD ["python3", "./app.py"]

