import boto3
import botocore
import os

BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

s3 = boto3.client('s3')

#Check versioning of the bucket. 
versioning = s3.get_bucket_versioning(
    Bucket=BUCKET_NAME
)

if versioning["Status"] != "Enabled":
	raise ValueError(f'Versioning is disabled on bucket: {BUCKET_NAME}')