from google.cloud import storage
import pandas as pd
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:/Users/lenovo/Desktop/DataTalks/week1/GCP & Terraform/MY_CREDENTIALS.JSON'



def create_bucket(bucket_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    bucket.storage_class ='standard'
    client.create_bucket(bucket, location='us-central1')

    return f'Bucket {bucket_name} created successfuly'


def upload_to_gcs (bucket_name,source_file, destenation_file):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destenation_file)
    blob.upload_from_file(source_file)

    return f'file {source_file} uploaded successfuly'


