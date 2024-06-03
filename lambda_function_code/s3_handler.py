import boto3
from datetime import datetime

s3 = boto3.client('s3')

def upload_to_s3(bucket: str, qr_code: BytesIO, qr_code_key: str) -> str:
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    s3_key = f'qrcodes/{qr_code_key}_{timestamp}.png'
    
    s3.put_object(
        Bucket=bucket,
        Key=s3_key,
        Body=qr_code.getvalue(),
        ContentType='image/png'
    )
    
    return f'arn:aws:s3:::{bucket}/{s3_key}'