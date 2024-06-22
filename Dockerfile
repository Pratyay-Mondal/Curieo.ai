# create a dockerfile for python cli app
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY . .

ENTRYPOINT ["python", "main.py"]