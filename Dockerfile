FROM python:3.9-slim-buster

COPY . /app
WORKDIR /app

RUN python3 -m pip install -U gTTS==2.2.3
RUN python3 -m pip install -U "discord.py[voice]"
RUN apt-get -y update
RUN apt-get install -y ffmpeg

ENTRYPOINT python3 main.py
