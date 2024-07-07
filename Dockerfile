# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install alembic


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt



RUN apt-get update

EXPOSE 5000


CMD ["python", "./application.py"]