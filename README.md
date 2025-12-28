## api-ui-microservices-docker-compose ##
This project demonstrates a complete CI/CD pipeline for microservices using Docker Compose, Jenkins, and GitHub. It includes a simple UI service (HTML frontend) and API service (Flask backend) deployed together.[1]
## Project Structure ##
api-ui-microservices-docker-compose/
├── ui-service/
│   ├── index.html
│   └── Dockerfile
├── api-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
└── Jenkinsfile

The structure separates UI (frontend) and API (backend) services with dedicated Dockerfiles and a unified Compose file for orchestration.
## UI Service (Frontend) ##
•	index.html: Simple static HTML page serving as the user interface, likely with API calls to the backend.
•	Dockerfile: Builds a lightweight container from the HTML file, using a web server like nginx or serving directly.
## API Service (Backend) ##
•	app.py: Flask-based Python application handling API endpoints.
•	requirements.txt: Lists dependencies (e.g., Flask) for the Python environment.
•	Dockerfile: Creates a Python container, installs dependencies, and exposes the API port.
## Docker Compose Setup ##
The docker-compose.yml orchestrates both services:
•	Links UI and API containers for inter-service communication.
•	Defines ports, volumes, and networks for local development and testing.
•	Enables running docker-compose up to start the full stack.
## Jenkins CI/CD Pipeline ##
Jenkinsfile automates:
•	Code checkout from GitHub.
•	Building Docker images for both services.
•	Running tests and validations.
•	Pushing images to Docker Hub.
•	Deploying containers via Docker Compose.
## Validation Steps ##
•	Pipeline execution shows console output, image creation, and container status.
•	Browser tests confirm UI and API functionality.
•	check Docker Hub registry