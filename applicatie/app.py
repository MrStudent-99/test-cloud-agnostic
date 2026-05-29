from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    cloud = os.getenv("CLOUD_PROVIDER", "kubernetes")
    hostname = os.getenv("HOSTNAME", "local")
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Cloud Agnostic POC</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }}
            .container {{
                background: white;
                border-radius: 12px;
                box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
                padding: 40px;
                max-width: 600px;
                text-align: center;
            }}
            h1 {{
                color: #333;
                margin-bottom: 10px;
                font-size: 2.5em;
            }}
            .subtitle {{
                color: #666;
                font-size: 1.1em;
                margin-bottom: 30px;
            }}
            .info-box {{
                background: #f5f5f5;
                border-left: 4px solid #667eea;
                padding: 20px;
                margin: 20px 0;
                text-align: left;
                border-radius: 6px;
            }}
            .info-box p {{
                margin: 10px 0;
                color: #333;
            }}
            .label {{
                font-weight: bold;
                color: #667eea;
            }}
            .status {{
                display: inline-block;
                background: #4CAF50;
                color: white;
                padding: 10px 20px;
                border-radius: 20px;
                margin: 20px 0;
                font-weight: bold;
            }}
            footer {{
                margin-top: 30px;
                color: #999;
                font-size: 0.9em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>☁️ Cloud Agnostic POC</h1>
            <p class="subtitle">Running on Kubernetes with GitOps</p>

            <div class="status">✓ Application Running</div>

            <div class="info-box">
                <p><span class="label">Cloud Provider:</span> {cloud.upper()}</p>
                <p><span class="label">Pod:</span> {hostname}</p>
                <p><span class="label">Timestamp:</span> {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
                <p><span class="label">Environment:</span> Development</p>
            </div>

            <footer>
                <p>Deployed via ArgoCD • GitOps enabled</p>
            </footer>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
