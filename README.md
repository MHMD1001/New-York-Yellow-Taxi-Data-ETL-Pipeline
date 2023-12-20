# Project Overview

## Description

This project is a data pipeline designed to pull New York Yellow Taxi trip records for the year 2022 from the TLC Trip Record Data website. The extracted data is ingested into a PostgreSQL database. The project includes various components, such as Docker configurations, Airflow setup, and Python scripts for data ingestion.
The project serves a dual purpose – ensuring operational efficiency with PostgreSQL and unlocking the power of BigQuery for advanced analytics. It's not just about storing data; it's about empowering data-driven decisions and insights

## Project Structure
### Docker Compose Configuration
#### Airflow Services
The docker-compose.yml file configures the Airflow services and dependencies. It includes PostgreSQL as the backend, Airflow webserver, scheduler, triggerer, and initialization services. Environment variables and volumes are defined for ease of configuration.

#### PostgreSQL and PgAdmin
For PostgreSQL and PgAdmin services, a separate docker-compose.yml file is provided. This includes configuration for a PostgreSQL database with specified credentials and a PgAdmin instance for database management.

### Airflow DAG Script
The data_ingestion_dag.py script defines the Airflow Directed Acyclic Graph (DAG) for the project. Tasks include downloading data with a BashOperator, ingesting data into PostgreSQL with a PythonOperator, uploading to GCS with a LocalFilesystemToGCSOperator, and creating a BigQuery external table with BigQueryCreateExternalTableOperator.

### .env Configuration
The '.env' file contains environment variables used by the Docker Compose configuration and Airflow DAG script. It includes Google Cloud credentials, connection details for PostgreSQL, and parameters for GCS and BigQuery.


## Usage
### Setting Up Environment
Ensure you have Docker and Docker Compose installed.

Create a service account on the Google Cloud Console with the following roles:

Storage Object Creator and Storage Object Viewer for Google Cloud Storage.
BigQuery Data Editor for managing datasets and tables in BigQuery.
Generate a JSON key file for the service account and save it securely.

### Update the .env file:

GOOGLE_APPLICATION_CREDENTIALS: Path to the downloaded JSON key file.
AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT: Update the key path in the connection string.
Adjust the configurations in the .env file, providing the necessary details for Google Cloud, PostgreSQL, and other variables.

## Running the Data Pipeline
1. Build Docker Images:
'''bash
  $docker-compose build
This command build our extended Airflow image defined by the dockerfile

2. Initialize Airflow:
'''bash
  $docker-compose up airflow-init
This commad to initialize the Airflow database and create the necessary tables and initial configuration

3. Start the Docker containers for Airflow using the appropriate Docker Compose files:
'''bash
  $docker-compose up -d

4. Start the Docker containers for PostgreSQL, and pgAdmin using the appropriate Docker Compose files:
'''bash
  $docker-compose up -d

5. Access the Airflow web interface at http://localhost:8080 and trigger the Data_ingestion_hh DAG.

6. Monitor the DAG execution in the Airflow web interface.

