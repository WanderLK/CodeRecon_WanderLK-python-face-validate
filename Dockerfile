FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update \
  && apt-get install -y python3 python3-distutils python3-pip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

RUN apt update \
  && apt-get install ffmpeg libsm6 libxext6 -y

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip

# Install Python dependencies
RUN pip3 install fastapi requests python-dotenv python-multipart opencv-python uvicorn

EXPOSE 8082

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8082"]
