FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir flask psutil
COPY app.py /app/app.py
EXPOSE 5000
CMD ["python","/app/app.py"]
HEALTHCHECK --interval=30s --timeout=3s --retries=3 CMD wget -qO- http://127.0.0.1:5000/healthz || exit 1
