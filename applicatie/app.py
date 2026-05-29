from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    cloud = os.getenv("CLOUD_PROVIDER", "unknown")
    return f"App is running on: {cloud}"

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
