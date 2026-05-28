# Dockerized Deployment

This project was containerized using Docker to ensure portability, dependency consistency, and simplified deployment workflows.

## Build Docker Image

docker build -t fastener-detection .

## Run Docker Container

docker run -p 8000:8000 fastener-detection

The application will run at:
http://localhost:8000

