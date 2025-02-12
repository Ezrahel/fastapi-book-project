# FastAPI Book Project

## 📌 Overview

This project is a FastAPI-based web application, containerized using Docker and deployed using Nginx as a reverse proxy. The application is designed to be scalable and easily deployable using Docker Compose and GitHub Actions for CI/CD.

## 📂 Project Structure

```
fastapi-book-project/
│── api/
    ├── db
    ├── routes
├── core/
│   ├── __pycache__
│   ├── __init__.py
│   ├── config.py
├── test/
│   ├── __pycache__
│   ├── .pytest_cache
│   ├── __init__.py
│── env
│── .gitignore
│── Dockerfile
│── Dockerfile.nginx
│── nginx.conf
│── requirements.txt
│── docker-compose.yml
│── .github/workflows/deploy.yml
│── README.md
```

## 🚀 Features

- FastAPI for high-performance APIs
- Dockerized setup for easy deployment
- Nginx reverse proxy for handling requests
- CI/CD pipeline with GitHub Actions
- Deployment on Azure Virtual Machine

## 🛠️ Prerequisites

Ensure you have the following installed before proceeding:

- Docker & Docker Compose
- Python 3.12+
- An Azure Virtual Machine (for deployment)
- GitHub account (for CI/CD pipeline)

## 🏗️ Local Setup

To run the FastAPI project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/fastapi-book-project.git
   cd fastapi-book-project
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  
   On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Run the FastAPI application:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

4. Open your browser and navigate to:

   ```
   http://127.0.0.1:8000/docs
   ```

## 🐳 Running with Docker

1. Build and run the FastAPI app with Docker:
   ```bash
   docker build -t fastapi-app .
   docker run -p 8000:8000 fastapi-app
   ```
2. Open your browser and check:
   ```
   http://localhost:8000/docs
   ```

## 🛠️ Using Docker Compose

To run the app along with Nginx:

```bash
docker-compose up --build -d
```

This starts both the FastAPI app and the Nginx reverse proxy.

## 📦 Pushing to Docker Hub

1. Tag the image:
   ```bash
   docker tag fastapi-app your-dockerhub-username/fastapi-app:latest
   ```
2. Push the image:
   ```bash
   docker push your-dockerhub-username/fastapi-app:latest
   ```

## 🚀 Deployment on Azure VM

1. SSH into your Azure VM:
   ```bash
   ssh -i private_key.pem your-user@your-vm-ip
   ```
2. Pull the latest image:
   ```bash
   docker pull your-dockerhub-username/fastapi-app:latest
   ```
3. Restart the containers:
   ```bash
   cd ~/fastapi-book-project
   docker-compose down
   docker-compose up --build -d
   ```

## 🔄 CI/CD with GitHub Actions

A **GitHub Actions workflow** automates deployment when code is pushed to the `main` branch.

### GitHub Secrets to Set Up:

- `SERVER_HOST`: Your Azure VM IP
- `SERVER_USER`: Your VM username
- `SERVER_SSH_KEY`: Your private SSH key

## 📜 API Documentation

FastAPI provides automatic documentation:

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **Redoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributions

Feel free to open issues and submit PRs if you want to contribute!

## ✉️ Contact

For any questions or support, reach out to [your-email@example.com](mailto\:your-email@example.com).

