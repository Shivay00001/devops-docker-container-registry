FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir flask gunicorn

COPY . .

EXPOSE 5000

ENTRYPOINT ["python", "src/main.py"]