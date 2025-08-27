from kafka import KafkaProducer
import json


class Producer:
    def __init__(self):
        self.producer = self.get_producer_config()

    def get_producer_config(self):
        try:
            # The Producer object requires the Kafka server, Json serializer
            producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                     api_version=(0, 11, 5),
                                     value_serializer=lambda x:
                                     json.dumps(x).encode('utf-8'))
            return producer
        except Exception as e:
            raise Exception(f"Error configuring Kafka producer: {e}")


    def publish(self, topic, event):
        self.producer.send(topic, event)

    def flush(self):
        self.producer.flush()


