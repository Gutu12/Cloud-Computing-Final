import csv

from google.cloud import pubsub_v1
from google.cloud import storage

project_id = 'traffic-flow-analysis-383122'
topic_name = 'TrafficFlow_optimizer'
bucket_name = 'trafficflow_bucket'
file_name = 'merged4_data.csv'

# Create a client to interact with Pub/Sub
publisher_client = pubsub_v1.PublisherClient()

# Get the bucket object
client = storage.Client()
bucket = client.get_bucket(bucket_name)

# Get the blob object for the file
blob = bucket.blob(file_name)

# Read the file as CSV
file_content = blob.download_as_string().decode('utf-8')
csv_reader = csv.DictReader(file_content.splitlines())

# Loop through the CSV rows and publish messages
for row in csv_reader:
    num_vehicles = int(row['numVehicles'])
    month = row['month']
    weekday = row['weekDay']
    if num_vehicles > 2000:
        message = f"Road is congested with {num_vehicles} vehicles on {weekday} in {month}. Find a different route."
        message_bytes = message.encode('utf-8')
        topic_path = publisher_client.topic_path(project_id, topic_name)
        future = publisher_client.publish(topic_path, data=message_bytes)
        print(f"Published message: {message} with message ID: {future.result()}")
