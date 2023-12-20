# Project Overview

## Description

This comprehensive project automates the Extraction, Transformation, and Loading (ETL) process for the New York Yellow Taxi trip records throughout 2022. Leveraging the TLC Trip Record Data website, the pipeline orchestrates a series of tasks, including data download, ingestion into a PostgreSQL database, upload to Google Cloud Storage (GCS), and the creation of a BigQuery external table referencing the GCS stored data.  
The project serves a dual purpose – ensuring operational efficiency with PostgreSQL and unlocking the power of BigQuery for advanced analytics. It's not just about storing data; it's about empowering data-driven decisions and insights.

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
1. Ensure you have Docker and Docker Compose installed.
2. Create a service account on the Google Cloud Console with the following roles:  
  a. Storage Object Creator and Storage Object Viewer for Google Cloud Storage.  
  b. BigQuery Data Editor for managing datasets and tables in BigQuery.  
  c. Generate a JSON key file for the service account and save it securely.  


### Update the .env file:

#### GOOGLE_APPLICATION_CREDENTIALS: Path to the downloaded JSON key file.  
#### AIRFLOW_CONN_GOOGLE_CLOUD_DEFAULT: Update the key path in the connection string.  
#### Adjust the configurations in the .env file, providing the necessary details for Google Cloud, PostgreSQL, and other variables.

### Running the Data Pipeline
1. Clone the repository:
```bash
  git clone https://github.com/MHMD1001/New-York-Yellow-Taxi-Data-ETL-Pipeline.git
```

2. Build Docker Images:
```bash
 docker-compose build
```
  This command build our extended Airflow image defined by the dockerfile

3. Initialize Airflow:
```bash
  $docker-compose up airflow-init
```
  This commad to initialize the Airflow database and create the necessary tables and initial configuration

4. Start the Docker containers for Airflow using the appropriate Docker Compose files:
```bash
docker-compose up -d
```

5. Start the Docker containers for PostgreSQL, and pgAdmin using the appropriate Docker Compose files:
```bash
  $docker-compose up -d
```

6. Access the Airflow web interface at http://localhost:8080 and trigger the Data_ingestion_hh DAG.

7. Monitor the DAG execution in the Airflow web interface.

## Important Notes
1. The DAG is scheduled to run monthly (@monthly), pulling data for each month of 2022.
2. Make sure to adjust file paths, URLs, and other parameters in the scripts and configurations based on your environment.
2. Feel free to explore and modify the project based on your specific requirements. If you encounter any issues or have questions, refer to the documentation or reach out for assistance.

Happy Data Pipelining!









