FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir  -r requirements.txt

RUN env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY .env .
CMD ["python", "main.py"]
