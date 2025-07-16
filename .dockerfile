FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY traffic_analyzer.py .
COPY sample-log.log .  # Optional: include a sample log for testing

CMD ["python", "traffic_analyzer.py"]