from google.cloud import pubsub_v1
from google.cloud import storage
project_id = 'traffic-flow-analysis-383122'
subscription_name = 'flow_sub'
# Create a client to interact with Pub/Sub
subscriber_client = pubsub_v1.SubscriberClient()

# Define the callback function
def callback(message):
    print(f"Received message: {message.data.decode('utf-8')}")
    message.ack()

# Create the subscription
subscription_path = subscriber_client.subscription_path(project_id, subscription_name)
subscription = subscriber_client.subscribe(subscription_path, callback=callback)

# Keep the main thread from exiting to allow the subscriber to continue listening for messages
try:
    subscription.result()
except KeyboardInterrupt:
    subscription.cancel()
