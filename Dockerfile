# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app source code
COPY app ./app

# Expose port 5000 (Flask default)
EXPOSE 5000

# Command to run the app
CMD ["python", "app/main.py"]
