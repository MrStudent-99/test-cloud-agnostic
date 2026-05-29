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
        <title>Cloud-agnostic POC</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;500;700&display=swap');

            * {{ margin: 0; padding: 0; box-sizing: border-box; }}

            body {{
                font-family: 'Ubuntu', sans-serif;
                background: #0f172a;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }}

            .container {{
                background: #ffffff;
                border-radius: 16px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.25);
                padding: 50px;
                max-width: 650px;
                width: 90%;
                text-align: center;
            }}

            h1 {{
                font-family: 'Ubuntu', sans-serif;
                font-weight: 700;
                color: #0f172a;
                margin-bottom: 8px;
                font-size: 2.6rem;
            }}

            .subtitle {{
                font-family: 'Ubuntu', sans-serif;
                font-weight: 300;
                color: #64748b;
                margin-bottom: 30px;
            }}

            .info-box {{
                background: #f8fafc;
                border-left: 4px solid #326ce5;
                padding: 20px;
                margin: 20px 0;
                border-radius: 8px;
                text-align: left;
            }}

            .info-box p {{
                margin: 12px 0;
                color: #334155;
            }}

            .label {{
                font-weight: 700;
                color: #326ce5;
            }}

            .status {{
                display: inline-block;
                background: #16a34a;
                color: white;
                padding: 12px 24px;
                border-radius: 999px;
                margin: 20px 0;
                font-family: 'Ubuntu', sans-serif;
                font-weight: 500;
            }}

            footer {{
                margin-top: 30px;
                color: #94a3b8;
                font-size: 0.9rem;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>☁️ Cloud-agnostic POC</h1>
            <p class="subtitle">Running on Kubernetes with GitOps</p>

            <div class="status">✓ Application Running</div>

            <div class="info-box">
                <p><span class="label">Cloud Provider:</span> {cloud.upper()}</p>
                <p><span class="label">Pod:</span> {hostname}</p>
                <p><span class="label">Timestamp:</span> {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
                <p><span class="label">GitOps:</span> ArgoCD</p>
                <p><span class="label">Container:</span> Docker</p>
                <p><span class="label">Orchestrator:</span> Kubernetes</p>
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
