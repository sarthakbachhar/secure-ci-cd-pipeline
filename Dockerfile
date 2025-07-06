# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Upgrade pip & setuptools first (to secure versions)
RUN pip install --upgrade pip setuptools

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the source code
COPY app ./app

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app/main.py"]
