FROM python:3.8-slim

WORKDIR /app

COPY app/gs_service.py /app/gs_service.py
COPY app/requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y ghostscript
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "gs_service.py"]
