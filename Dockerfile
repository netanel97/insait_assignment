# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN apt-get update \
    && apt-get -y install libpq-dev gcc postgresql-client \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Environment variable to switch between running the app and tests
ENV RUN_TESTS=false

# Command to run the application or tests
CMD sleep 10 && \
    alembic upgrade head && \
    python ./app.py