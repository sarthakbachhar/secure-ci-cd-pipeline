# Secure CI/CD Pipeline with Flask, Bandit, and Trivy

This project demonstrates a secure CI/CD pipeline implementation for a basic Python Flask web application. The application is containerized using Docker and integrated with GitHub Actions to perform static analysis and vulnerability scanning as part of the deployment workflow.

The project merges fundamental concepts from both cybersecurity and DevOps, aligning with modern DevSecOps practices.

---

## Features

- Static code analysis using Bandit
- Dockerized Python Flask application
- CI/CD pipeline configured with GitHub Actions
- Vulnerability scanning of Docker images using Trivy
- Simple web interface rendered through Flask and HTML templates

---

## Project Structure


secure-ci-cd-pipeline/
- app/
  - main.py # Flask app
  - templates/
    - index.html # HTML template for web interface
- tests/
  - test_app.py # Unit test for the Flask app
- Dockerfile # Docker image definition
- requirements.txt # Python dependencies
- .github/
  - workflows/
    - ci.yml # CI/CD pipeline definition


---

## CI/CD Pipeline Flow

The GitHub Actions workflow runs on every push or pull request to the `main` branch. It performs the following steps:

1. Checkout the source code
2. Set up Python environment
3. Install project dependencies
4. Run unit tests
5. Scan for hardcoded secrets using Gitleaks
6. Build a Docker image of the Flask app
7. Scan the Docker image for vulnerabilities using Trivy
8. Perform static code analysis using Bandit

---

## How to Run Locally

### Prerequisites

- Python 3.9+
- Docker

### Run with Docker

docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app

Then open: http://localhost:5000
