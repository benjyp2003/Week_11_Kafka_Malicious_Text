from kafka import KafkaConsumer
import json
import os


class ConsumerConfig:

    @staticmethod
    def get_consumer_events(topic1,topic2):
        kafka_url = os.getenv('KAFKA_URL', 'localhost')
        kafka_port = os.getenv('KAFKA_PORT', '9092')
        group_id = os.getenv('KAFKA_GROUP_ID', 'my-group')
        bootstrap_servers = [f'{kafka_url}:{kafka_port}']

        consumer = KafkaConsumer(topic1,topic2,
                                 group_id=group_id,
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=bootstrap_servers)

        return consumer
