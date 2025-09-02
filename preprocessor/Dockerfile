FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements file
COPY preprocessor/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the utils module (shared dependency)
COPY utils/ ./utils/

# Copy the preprocessor service code
COPY preprocessor/ ./

# Copy test script
#COPY test_imports.py ./

WORKDIR /app/app
ENV PYTHONPATH=/app
ENV SERVICE_NAME=preprocessor

# Test imports before starting the service
CMD ["sh", "-c", "cd /app && cd /app/app && python manager.py"]