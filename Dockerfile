# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set environment variables to avoid writing .pyc files and to run Python in unbuffered mode
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies (optional, add more if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of your project code into the container
COPY . /app/

# Collect static files (if using WhiteNoise or similar)
RUN python manage.py collectstatic --noinput

# Expose the port the app will run on
EXPOSE 8000

# Use Gunicorn as the production server
CMD ["gunicorn", "djangoproject.wsgi:application", "--bind", "0.0.0.0:8000"]
