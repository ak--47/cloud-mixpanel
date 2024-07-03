
import os
from google.cloud import storage # pip install google-cloud-storage 

# important! replace these variables with your values
bucket_name = 'mixpanel-mcd-pos-poc'
source_file_name = 'source_file.json'
destination_blob_name = 'destination_file.json'
key_file_path = 'keyfile.json'

def upload_to_bucket(bucket_name, source_file_name, destination_blob_name, key_file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    key_file_resolved_path = os.path.join(script_dir, key_file_path)
    source_file_resolved_path = os.path.join(script_dir, source_file_name)

    # Initialize a client
    storage_client = storage.Client.from_service_account_json(key_file_resolved_path)

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # Create a blob object from the bucket
    blob = bucket.blob(destination_blob_name)

    # Upload the file to the blob
    blob.upload_from_filename(source_file_resolved_path)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")


# Upload the file
upload_to_bucket(bucket_name, source_file_name, destination_blob_name, key_file_path)

