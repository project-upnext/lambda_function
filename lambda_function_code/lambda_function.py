import json
import logging
from datetime import datetime
import boto3

from config import S3_BUCKET, DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT
from s3_handler import upload_to_s3
from database_handler import DatabaseHandler

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        qr_code_key = event['qrCodeKey']
        business_email = event['businessEmail']
        
        qr_code_image = generate_qr_code(qr_code_key, business_email)
        
        s3_arn = upload_to_s3(S3_BUCKET, qr_code_image, qr_code_key)
        
        db_handler = DatabaseHandler(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT)
        
        db_handler.insert_qr_code_and_arn(s3_arn, business_email)
        
        # Return a success response
        return {
            'statusCode': 200,
            'body': json.dumps('QR code generated and uploaded successfully')
        }
        
    except Exception as e:
        logger.error(f"Error generating or uploading QR code: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error generating or uploading QR code')
        }
