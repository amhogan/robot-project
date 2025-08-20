FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir flask psutil
WORKDIR /app
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
