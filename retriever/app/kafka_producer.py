from kafka import KafkaProducer
import json
from bson import ObjectId
from datetime import datetime
import os

class Producer:
    def __init__(self):
        self.producer = self.get_producer_config()

    def get_producer_config(self):
        try:
            kafka_url = os.getenv('KAFKA_URL', 'localhost')
            kafka_port = os.getenv('KAFKA_PORT', '9092')
            bootstrap_servers = [f'{kafka_url}:{kafka_port}']
            producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                     value_serializer=lambda x:
                                     json.dumps(x, default=self.json_serializer).encode('utf-8'))

            return producer

        except Exception as e:
            raise Exception(f"Error configuring Kafka producer: {e}")

    def json_serializer(self, obj):
        """Custom JSON serializer for MongoDB ObjectId and datetime objects"""
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    def publish(self, topic, event):
        self.producer.send(topic, event)

    def flush(self):
        self.producer.flush()