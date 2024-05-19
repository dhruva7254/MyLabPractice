import json
import boto3
import os

def lambda_handler(event, context):
    
    s3 = boto3.client("s3")
    
    try:
        bucket = os.environ.get('s3_bucket')
        print(bucket)
        key = "incoming/empty_incoming.txt"
        
        download_dir = "/tmp/"
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        
        download_path = "/tmp/{}".format(key.split('/')[-1])
        s3.download_file(bucket, key, download_path)
        
        processed_file_key = key.split('.')[0] + '_processed_file.' + key.split('.')[1]
        print("processed_file_key:",processed_file_key)
        
        output_bucket = os.environ.get('s3_bucket')
        output_key = 'output/{}'.format(processed_file_key.split('/')[-1])
        s3.upload_file(download_path, bucket, output_key)
        return {
        'statusCode': 200,
        'body': 'File processed and uploaded successfully!'
            }
    except Exception as e:
        print(e)