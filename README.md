# Secure CI/CD Pipeline with Flask, Docker, and GitHub Actions

This project demonstrates how to build a secure and automated CI/CD pipeline using a simple Python Flask application. The pipeline includes code testing, secret scanning, static analysis, Docker image building, and vulnerability scanning — all handled automatically via GitHub Actions.

## Features

- Flask-based web application (returns "Hello Secure CI/CD")
- Dockerized application for consistent deployment
- Automated CI/CD using GitHub Actions
- Unit testing using Python's `unittest`
- Secret scanning using Gitleaks
- Static code analysis using Bandit
- Container vulnerability scanning using Trivy

---

## Technologies Used

- Python 3.9
- Flask
- Docker
- GitHub Actions
- Gitleaks
- Bandit
- Trivy

---

## Project Structure

secure-ci-cd-pipeline/
├── app/
│ └── main.py # Flask app
├── tests/
│ └── test_app.py # Unit test for the Flask app
├── Dockerfile # Docker image definition
├── requirements.txt # Python dependencies
└── .github/
└── workflows/
└── ci.yml # CI/CD pipeline definition


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

### Run without Docker

```bash
pip install -r requirements.txt
python app/main.py

Open your browser and visit: http://localhost:5000

docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app

Then open: http://localhost:5000
