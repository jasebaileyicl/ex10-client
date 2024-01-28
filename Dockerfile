# Use the official Python image as a base image
FROM python:3.11

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app /app

EXPOSE 5000

# Define environment variable
ENV FLASK_APP app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]