# tests/test_main.py
# Actual tests for our Flask app — making sure the routes work as expected

import sys
import os
import pytest

# we need to add the parent dir to sys.path so Python can find our app module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app


@pytest.fixture
def client():
    """Spin up a test client so we can hit our routes without running the server."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_returns_200(client):
    """The homepage should load without any issues."""
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_expected_content(client):
    """Make sure the landing page actually has our project title in it."""
    response = client.get("/")
    html = response.data.decode("utf-8")
    assert "Secure CI/CD Pipeline" in html


def test_home_mentions_tools(client):
    """The page should list the security tools we're using."""
    response = client.get("/")
    html = response.data.decode("utf-8")
    assert "Gitleaks" in html
    assert "Bandit" in html
    assert "Trivy" in html


def test_nonexistent_route_returns_404(client):
    """Hitting a route that doesn't exist should give us a 404, not a crash."""
    response = client.get("/this-page-doesnt-exist")
    assert response.status_code == 404
