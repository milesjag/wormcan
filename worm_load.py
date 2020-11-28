import psycopg2
import boto3
import io


def get_s3_object(bucket: str, key: str) -> str:
    """
    Downloads S3 file and returns as decoded string
    """
    client = boto3.client("s3")
    s3_object = client.get_object(Bucket=bucket, Key=key)
    s3_object = io.BytesIO(s3_object["Body"].read()).read().decode("utf-8")
    return s3_object


def delete_s3_object(bucket: str, key: str):
    """
    Deletes an object from S3
    """
    client = boto3.client("s3")
    client.delete_object(Bucket=bucket, Key=key)
    return


def put_s3_object(file_string: str, bucket: str, key: str) -> None:
    """
    Uploads string as S3 file
    """
    client = boto3.client("s3")
    buffered_object = io.BytesIO(file_string.encode("utf-8"))
    response = client.upload_fileobj(buffered_object, bucket, key)
    return


def get_rdbms_credentials():
    """
    Get RDBMS credentials
    """
    return {
        "database": "worms",
        "user": "k2",
        "password": "zaqxswcde123",
        "host": "127.0.0.1",
        "port": 5432,
    }


def execute_query(query: str) -> None:
    """
    Execute and commit a query remotely
    """
    credentials = get_rdbms_credentials()
    with psycopg2.connect(**credentials) as connection:
        cursor = connection.cursor
        cursor.execute(query)
    return
