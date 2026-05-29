FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask
ENV CLOUD_PROVIDER="local"
CMD ["python", "app.py"]