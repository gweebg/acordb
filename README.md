# Acordb

O Acordb é uma aplicação web para gestão de acórdãos (decisões judiciais) de varios tribunais nacionais. Esta aplicação dá um interface amigavel ao utilizador que permite gerir,pesquisar,analisar dados de um acordão. O sistema foi construido usando uma REST Api em Django e Svelt kit para frontent.

## Features

- User authentication and authorization
- Uploading and indexing acórdãos from multiple tribunals
- Advanced search functionality to find specific acórdãos
- Data analysis and visualization tools
- Integration with external APIs for additional data sources (if applicable)
- Responsive and intuitive user interface

## Prerequisites

Before running the Acórdãos Management System, ensure you have the following prerequisites installed:

- Docker
- Docker Compose

## Installation

1. Clone the repository:
git clone https://github.com/your-username/acordaos-management-system.git
cd acordaos-management-system

2. Build and start the Docker containers:

docker-compose up --build

This command will build the necessary Docker images and start the backend, frontend, MongoDB, and PostgreSQL services.

3. Access the application in your web browser at `http://localhost/`.

## Usage

- The backend service (Django) runs on `http://localhost:8000`.
- The frontend service (Svelt Kit) runs on `http://localhost:80`.
- MongoDB is accessible at `mongodb://localhost:27017`.
- PostgreSQL is accessible at `postgresql://localhost:5432`.


## Deployment

- Configure a production-ready web server (e.g., Nginx or Apache) to serve the Django backend.
- Set up a reverse proxy to forward requests to the appropriate backend service.
- Configure and secure the databases (MongoDB and PostgreSQL) for production use.
- Use environment variables or configuration files to manage sensitive information securely.
- Implement a logging mechanism to monitor and track system activities.

## Configuration

The Acórdãos Management System provides several configuration options. Some key configuration files include:

- `settings.py`: Configure the Django settings for the backend, including database connections, static files, and more.
- `docker-compose.yml`: Define the services, networks, and volumes for the Docker containers.
- `.env`: Store environment variables used by the system (e.g., secret keys, database credentials).

