import boto3
import botocore
import os

BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
# BUCKET_NAME = 'circleci-sergiu-raduleae'

s3 = boto3.client('s3')

#Check versioning of the bucket. 
versioning = s3.get_bucket_versioning(
    Bucket=BUCKET_NAME
)

print(versioning)

try:
	if versioning["Status"] == "Enabled":
		print(f'Versioning is enabled on bucket: {BUCKET_NAME}')
except:
	raise ValueError(f'Versioning is disabled on bucket: {BUCKET_NAME}')


hosting = s3.get_bucket_website(
    Bucket=BUCKET_NAME
)

print(hosting)