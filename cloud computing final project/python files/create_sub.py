from google.cloud import pubsub_v1

project_id = 'traffic-flow-analysis-383122'
topic_name = 'TrafficFlow_optimizer'
subscription_name = 'flow_sub'

# Create a client to interact with Pub/Sub
publisher_client = pubsub_v1.PublisherClient()
subscriber_client = pubsub_v1.SubscriberClient()

# Check if the topic already exists
topic_path = publisher_client.topic_path(project_id, topic_name)
try:
    topic = publisher_client.get_topic(request={"topic": topic_path})
except:
    # Create the topic if it doesn't exist
    topic = publisher_client.create_topic(request={"name": topic_path})

# Check if the subscription already exists
subscription_path = subscriber_client.subscription_path(project_id, subscription_name)
try:
    subscription = subscriber_client.get_subscription(request={"subscription": subscription_path})
except:
    # Create the subscription if it doesn't exist
    subscription = subscriber_client.create_subscription(request={"name": subscription_path, "topic": topic_path})

