
# Analytics and Monitoring

This service is responsible for monitoring and analytics within the Squares AI platform, including performance metrics, logs and visualizations.

## Features
- Collects and analyzes performance metrics for AI models.
- Provides visualization dashboards for real-time monitoring.
- Stores logs and metrics in a PostgreSQL database.

## Getting Started

### Prerequisites
- Docker and Docker Compose installed.
- Python 3.10 (for local development).

### Setup
1. Clone this repository.
2. Build and start the services using Docker Compose:

```bash
docker-compose up --build
```

3. Access the service at `http://localhost:8000`.

### Directory Structure
- `src/`: Source code for analytics and monitoring services.
- `tests/`: Unit and integration tests.
- `data/`: Data and logs (mounted as a Docker volume).

## Contributing
Contributions are welcome! Please submit a pull request or create an issue.
    