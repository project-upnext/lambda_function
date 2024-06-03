# QR Code Generator Lambda Function

This AWS Lambda function generates a QR code from provided data and a business email, uploads the QR code image to an S3 bucket, and stores the S3 ARN in an RDS MySQL database. This project is structured to follow best coding practices with modular components for configuration, QR code generation, S3 operations, and database interactions.

## Project Structure
    ├── config.py
    ├── database_handler.py
    ├── qr_code_generator.py
    ├── s3_handler.py
    ├── lambda_function.py
    ├── requirements.txt


## Requirements
-   Python 3.8 or higher
-   AWS Lambda
-   PostgreSQL
-   boto3
-   pymysql
-   qrcode