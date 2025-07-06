# app/main.py

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Secure CI/CD!"

if __name__ == "__main__":
    app.run(debug=True)
