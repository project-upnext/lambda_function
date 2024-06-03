import psycopg2
from psycopg2 import sql

import psycopg2
from psycopg2 import sql

class DatabaseHandler:
    def __init__(self, host, user, password, db_name, port):
        self.connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            dbname=db_name,
            port=port
        )
    
    def insert_qr_code_and_arn(self, s3_arn: str,business_email: str):
        try:
            with self.connection.cursor() as cursor:
                
                update_query = sql.SQL("UPDATE business SET s3Arn = %s WHERE businessEmail = %s")
                cursor.execute(update_query, (s3_arn, business_email))
                self.connection.commit()
        finally:
            self.connection.close()