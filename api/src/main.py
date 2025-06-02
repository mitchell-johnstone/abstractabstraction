from datetime import datetime
from fastapi import FastAPI
from mangum import Mangum
import boto3
import json


BUCKET_NAME = "abstractabstraction-data"
REGION = "us-east-2"
TEST_FILE_NAME = "test_obj.json"

s3 = boto3.client("s3")

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Lambda"}


@app.get("/upload")
def upload():
    # Get the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    json_data = {"current_time": current_time}
    s3.put_object(
        Body=json.dumps(json_data),
        Bucket=BUCKET_NAME,
        Key=TEST_FILE_NAME,
        ContentType="application/json",
    )
    return {"message": "successful upload!"}


@app.get("/download")
def download():
    content = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=TEST_FILE_NAME,
    )
    return content["Body"].read().decode("utf-8")


handler = Mangum(app)
