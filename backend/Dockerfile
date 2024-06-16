# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port for the Flask app
EXPOSE 5000

# Set the entry point for the container
CMD ["python", "app.py"]