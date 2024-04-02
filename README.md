# iot-data-engine

thingspeaks-data-engine is a powerful tool designed to fetch data from ThingSpeak, normalize it, and store it into a relational database. It serves as an API that allows users to configure the engine and ingest data seamlessly.

## Getting Started

To get started with thingspeaks-data-engine, follow these steps:

### Development

1. Navigate to the `app` directory.
2. Activate the virtual environment using Poetry:
    ```bash
    poetry shell
    ```
3. Run the engine:
    ```bash
    python3 run_engine.py
    ```

### Deployment

1. Build and deploy using Docker Compose:
    ```bash
    docker-compose up --build -d
    ```

## Usage

iot-data-engine exposes the following endpoints:

- `/configuration`: Configure the engine with the desired ThingSpeak channel and token.
- `/ingest`: Start data ingestion with the provided ThingSpeak channel ID as a query parameter, and the following JSON payload:
  ```json
  {
    "n_rows": 100,
    "interval": 50
  }
  
- `/`:Get information about the developer.

## Examples:

1. **Configure Engine**
    ```bash
    curl -X POST 'http://127.0.0.1:5000/configuration?channel=123456&token=XXXXYHUHHGG'
    ```

2. **Start Data Ingestion**
    ```bash
    curl -X POST -d '{"n_rows": 100, "interval": 50}' 'http://127.0.0.1:5000/ingest?channel=2057381'
    ```

## About the Developer

This project is developed and maintained by @fbzavaleta. For any inquiries or contributions, please contact [benjamin.zavaleta@grieletlabs.com].