import os
from airflow import DAG
from datetime import datetime , timedelta
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator
from ingest_data import ingest_function



url_prefix = "https://d37ci6vzurychx.cloudfront.net/trip-data"
ulr_template = url_prefix + "/yellow_tripdata_{{execution_date.strftime('%Y-%m')}}.parquet"
file_template = "/opt/airflow/yellow_taxi_data_{{execution_date.strftime('%Y_%m')}}.parquet"
object_template = "yellow_taxi_data_{{execution_date.strftime('%Y_%m')}}.parquet"
table_name = "trip_data_{{execution_date.strftime('%Y_%m')}}"
bucket_name = os.getenv('bucket_name')
project_id = os.getenv('project')
dataset_id = os.getenv('data_set')
user = os.getenv('user')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
db = os.getenv('database')



default_args = {
    'owner' : 'mhmd',
    'start_date' : datetime(2021, 12, 31),
    'end_date' : datetime(2022, 12, 30),
    'retries': 3,
    'retry_delay': timedelta(minutes=5) 
}


dag = DAG(
    'Data_ingestion_hh',
    default_args = default_args,
    schedule_interval = '@monthly'
)

download_command = f'curl -o {file_template} {ulr_template}'

with dag:

    download_data = BashOperator(
        task_id ='download_yellow_taxi_data',
        bash_command = download_command
    )



    data_ingestion = PythonOperator(
        task_id = 'ingest_data_to_postgres',
        python_callable = ingest_function,
        op_args =(user, password, host, port, db, table_name, file_template)
    )


    to_gcs_task = LocalFilesystemToGCSOperator(
        task_id ='uploading_data_to_gcs',
        src = file_template,
        bucket = bucket_name,
        dst = object_template
    )


    to_BigQuery_task = BigQueryCreateExternalTableOperator(
        task_id = 'Create_BigQuery_external_table',
        bucket = bucket_name,
        source_objects = [object_template],
        destination_project_dataset_table = f'{project_id}.{dataset_id}.{table_name}',
        source_format = 'parquet'
    )




    download_data >> [data_ingestion,to_gcs_task] >> to_BigQuery_task



