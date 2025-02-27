# FastAPI Book Management API

## Overview

This project is a RESTful API built with FastAPI for managing a book collection. It provides comprehensive CRUD (Create, Read, Update, Delete) operations for books with proper error handling, input validation, and documentation.

## Features

- 📚 Book management (CRUD operations)
- ✅ Input validation using Pydantic models
- 🔍 Enum-based genre classification
- 🧪 Complete test coverage
- 📝 API documentation (auto-generated by FastAPI)
- 🔒 CORS middleware enabled

## Project Structure

```
fastapi-book-project/
├── api/
│   ├── db/
│   │   ├── __init__.py
│   │   └── schemas.py      # Data models and in-memory database
│   ├── routes/
│   │   ├── __init__.py
│   │   └── books.py        # Book route handlers
│   └── router.py           # API router configuration
├── core/
│   ├── __init__.py
│   └── config.py           # Application settings
├── tests/
│   ├── __init__.py
│   └── test_books.py       # API endpoint tests
├── main.py                 # Application entry point
│── env
│── .gitignore
│── Dockerfile
│── Dockerfile.nginx
│── nginx.conf
│── docker-compose.yml
│── .github/workflows/deploy.yml
├── requirements.txt        # Project dependencies
└── README.md
```

## Technologies Used

- Python 3.12
- FastAPI
- Pydantic
- pytest
- uvicorn

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hng12-devbotops/fastapi-book-project.git
cd fastapi-book-project
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the server:

```bash
uvicorn main:app
```

2. Access the API documentation:

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Endpoints

### Books

- `GET /api/v1/books/` - Get all books
- `GET /api/v1/books/{book_id}` - Get a specific book
- `POST /api/v1/books/` - Create a new book
- `PUT /api/v1/books/{book_id}` - Update a book
- `DELETE /api/v1/books/{book_id}` - Delete a book

### Health Check

- `GET /healthcheck` - Check API status

## Book Schema

```json
{
  "id": 1,
  "title": "Book Title",
  "author": "Author Name",
  "publication_year": 2024,
  "genre": "Fantasy"
}
```

Available genres:

- Science Fiction
- Fantasy
- Horror
- Mystery
- Romance
- Thriller

## Running Tests

```bash
pytest
```

## Error Handling

The API includes proper error handling for:

- Non-existent books
- Invalid book IDs
- Invalid genre types
- Malformed requests

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


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
   uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
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


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue in the GitHub repository.


# FastAPI Book Project

## 📌 Overview

This project is a FastAPI-based web application, containerized using Docker and deployed using Nginx as a reverse proxy. The application is designed to be scalable and easily deployable using Docker Compose and GitHub Actions for CI/CD.

## 📂 Project Structure




## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributions

Feel free to open issues and submit PRs if you want to contribute!

## ✉️ Contact

For any questions or support, reach out to [your-email@example.com](mailto\:your-email@example.com).

