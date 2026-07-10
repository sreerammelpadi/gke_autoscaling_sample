FROM python:3.9-slim
WORKDIR /app
COPY producer/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY producer/main.py .
COPY traffic-config.json .
CMD ["python", "main.py"]
