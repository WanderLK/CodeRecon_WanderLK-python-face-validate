FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app

RUN apt-get update 

RUN pip install fastapi requests pymongo python-dotenv pydantic python-multipart opencv-python

COPY .env /app/.env
COPY . /app

EXPOSE 8082

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8082"]
