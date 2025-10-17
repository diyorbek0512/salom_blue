FROM python:3.11.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy only dependency files first for better caching
COPY req.txt /app/
COPY pyproject.toml /app/  

# Install system build dependencies needed for some Python packages
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential gcc libssl-dev libffi-dev libxml2-dev libxslt1-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
RUN python -m pip install --upgrade pip
RUN pip install -r req.txt

# Copy application code
COPY . /app

# Default command
CMD ["python", "app.py"]
