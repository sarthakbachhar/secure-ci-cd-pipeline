# app/main.py
# This is the Flask app — super simple on purpose.
# The real magic happens in the CI/CD pipeline, not here.

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Just serves the landing page. Nothing fancy."""
    return render_template("index.html")


if __name__ == "__main__":
    # binding to 0.0.0.0 so Docker can reach it from outside the container
    app.run(host="0.0.0.0", debug=False)  # nosec
