import os
import json
import requests
import boto3
from flask import Flask, jsonify
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Flask app
app = Flask(__name__)

# AWS Credentials & Bucket Name
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
API_URL = os.getenv("API_URL")  # Replace with actual API

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

def fetch_api_data():
    """Fetch data from an external API"""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.json()
    except requests.RequestException as e:
        print(f"API request failed: {e}")
        return None

def save_and_upload_to_s3():
    """Save API response to JSON and upload to S3"""
    data = fetch_api_data()
    if not data:
        return "Failed to fetch API data"

    # Generate a timestamped filename
    filename = f"nasdaq_roc60d_data_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"

    # Save JSON locally
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    # Upload to S3
    try:
        s3_client.upload_file(filename, S3_BUCKET_NAME, filename)
        return f"Uploaded {filename} to S3 bucket {S3_BUCKET_NAME}"
    except Exception as e:
        return f"Failed to upload to S3: {e}"

@app.route('/trigger', methods=['GET'])
def trigger():
    """API endpoint to trigger API call and S3 upload"""
    result = save_and_upload_to_s3()
    return jsonify({"message": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6002)
