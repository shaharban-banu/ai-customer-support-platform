# AI-Powered Customer Support Intelligence Platform

A cloud-native customer support platform built with **React, FastAPI, SQLite, Apache Kafka, Docker, Kubernetes, Helm, GitHub Actions, and Prometheus**.

The project provides a foundation for managing support tickets, deriving structured ticket insights, processing ticket events, and monitoring backend API performance.

## Overview

Customer support teams receive messages about payments, refunds, account access, deliveries, and technical issues. This project aims to organize ticket information and automate initial ticket analysis while providing a deployable and monitorable application architecture.

### Key Features

- REST API development using FastAPI
- Ticket persistence using SQLite and SQLAlchemy
- Rule-based ticket categorization
- Keyword-based sentiment detection
- Rule-based priority prediction
- Basic text summarization
- Kafka-based ticket event streaming
- React + Vite frontend
- Docker containerization and Docker Compose
- Kubernetes manifests and Helm chart resources
- GitHub Actions CI pipeline
- Prometheus metrics instrumentation
- Automated testing with pytest
- Code-quality checks with Pylint

## Technology Stack

| Component | Technology |
|---|---|
| Frontend | React, Vite |
| Backend | Python, FastAPI |
| Database | SQLite, SQLAlchemy |
| Event streaming | Apache Kafka, KRaft |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes |
| Packaging | Helm |
| CI/CD | GitHub Actions |
| Monitoring | Prometheus |
| Testing | pytest |
| Code quality | Pylint |
| API documentation | FastAPI Swagger UI |

## Architecture

```text
React + Vite Frontend
         |
         v
    FastAPI Backend
      /         \\
     v           v
 SQLite DB    Kafka Producer
                  |
                  v
           support-tickets
                  |
                  v
            Kafka Consumer

FastAPI --> Prometheus Metrics
GitHub Actions --> Tests and Docker Image Build/Push
Kubernetes + Helm --> Deployment Resources
```

> **Note:** The diagram represents the project's major components. The exact connection between Kafka consumption and ticket analysis should be verified in the implementation before describing it as a fully automated processing pipeline.

## Ticket Analysis

The backend's `ai_service.py` contains four analysis functions:

- **Ticket classification:** Categorizes messages into billing, refund, account, delivery, or technical using keyword rules.
- **Sentiment detection:** Labels messages Negative when configured negative keywords are present; otherwise, labels them Positive.
- **Priority prediction:** Assigns high priority when specified urgency keywords are detected; otherwise, assigns medium.
- **Summary generation:** Returns the first 50 characters of the message.

These functions currently use rule-based logic. Transformer-based sentiment analysis and summarization code is commented out, so the current implementation should not be described as a trained machine-learning inference pipeline.

## Database

The project uses SQLite through SQLAlchemy.

The `Ticket` model defines the following fields:

- `id`: Primary key
- `message`: Ticket message
- `category`: Classified ticket category
- `sentiment`: Detected sentiment
- `priority`: Assigned priority
- `summary`: Generated text excerpt

Database tables are initialized when the FastAPI application starts.

## Kafka Event Streaming

Apache Kafka is configured in KRaft mode using Docker Compose, with internal and external listeners.

The intended event flow is:

1. A ticket event is published to the `support-tickets` topic.
2. A Kafka consumer receives the event.
3. Downstream processing can analyze the ticket and persist its results.

Verify the producer, consumer, and analysis integration before claiming that all three steps execute automatically.

## Monitoring and Observability

The backend uses `prometheus-fastapi-instrumentator` to expose metrics at:

`http://localhost:8000/metrics`

The Prometheus configuration scrapes the `backend:8000/metrics` target every five seconds when the backend is reachable using that service name on the same network.

## CI/CD Pipeline

The GitHub Actions workflow includes:

1. Installing backend dependencies.
2. Running automated tests with pytest.
3. Running Pylint against the application package.
4. Building a backend Docker image after the test job succeeds.
5. Authenticating to Docker Hub using repository secrets.
6. Pushing the image tagged `v1`.

The configured Docker Hub credentials should be stored in GitHub Actions secrets rather than committed to the repository.

## Deployment Resources

The repository includes:

- `docker-compose.yml` for local multi-service setup
- A backend Dockerfile
- Kubernetes YAML resources
- A Helm chart with `Chart.yaml`, `values.yaml`, and templates
- `monitoring/prometheus.yml` for Prometheus scrape configuration

These resources support containerization and deployment workflows. Confirm successful deployment in each target environment before documenting it as currently running.

## Run Locally

### Prerequisites

- Python compatible with the backend requirements
- Docker and Docker Compose
- Node.js and npm for the frontend

### Start the backend and Kafka

From the project root:

```bash
docker compose up --build -d
docker compose ps
```

Inspect backend logs if a service does not start:

```bash
docker compose logs --tail=100 backend
```

### Open the API documentation

When the backend is running, visit:

- API documentation: `http://localhost:8000/docs`
- Metrics endpoint: `http://localhost:8000/metrics`

### Start the frontend

Open a terminal in the frontend directory containing `package.json`:

```bash
npm install
npm run dev
```

Use the local URL printed by Vite.

## Testing and Code Quality

Run the backend checks from the backend directory:

```bash
pytest
pylint app
```

The GitHub Actions workflow runs these checks as part of the CI pipeline.

## Project Structure

```text
customer_support_ai/
├── .github/
│   └── workflows/
│       └── ci.yml
├── backend/
│   ├── app/
│   │   ├── database/
│   │   ├── kafka/
│   │   ├── routes/
│   │   ├── schemas/
│   │   ├── ai_service.py
│   │   └── main.py
│   ├── tests/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── tickets.db
├── customer-support-ai/
│   ├── templates/
│   ├── charts/
│   ├── Chart.yaml
│   └── values.yaml
├── frontend/
├── monitoring/
│   └── prometheus.yml
├── docker-compose.yml
└── README.md
```

## Future Improvements

- Integrate the Kafka consumer with the ticket-analysis pipeline.
- Replace keyword heuristics with validated NLP models where appropriate.
- Improve neutral-sentiment handling and priority levels.
- Add robust error handling, logging, and integration tests.
- Validate monitoring targets and deployment manifests in their target environments.
- Add end-to-end tests covering ticket creation, analysis, and persistence.
