FROM python:3.10-slim
WORKDIR /app
COPY health_check.py .
CMD ["python", "health_check.py"]
