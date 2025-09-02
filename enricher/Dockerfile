#FROM python:3.11-slim
#
#ENV PYTHONUNBUFFERED=1
#
#WORKDIR /app
#
#COPY enricher/requirements.txt .
#
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY utils/ ./utils/
#
#COPY enricher/ ./
#
#WORKDIR /app/app
#ENV PYTHONPATH=/app
#CMD ["python", "app/app/manager.py"]
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy requirements file
COPY enricher/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('punkt')"

# Copy the utils module (shared dependency)
COPY utils/ ./utils/

# Copy the enricher service code
COPY enricher/ ./

# Copy test script
#COPY test_imports.py ./

WORKDIR /app/app
ENV PYTHONPATH=/app
ENV SERVICE_NAME=enricher

# Test imports before starting the service
CMD ["sh", "-c", "cd /app/app && python manager.py"]