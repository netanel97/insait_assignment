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


# Command to run the application
CMD alembic upgrade head && python ./app.py
