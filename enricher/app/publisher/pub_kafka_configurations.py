from kafka import KafkaProducer
import json
import os
class ProducerConfig:

    @staticmethod
    def get_producer():
        kafka_url = os.getenv('KAFKA_URL', 'localhost')
        kafka_port = os.getenv('KAFKA_PORT', '9092')
        bootstrap_servers = [f'{kafka_url}:{kafka_port}']
        producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                                 value_serializer=lambda x:
                                 json.dumps(x).encode('utf-8'))

        print(producer.config)
        return producer

