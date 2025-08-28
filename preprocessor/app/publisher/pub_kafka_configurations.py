from kafka import KafkaProducer
import json

class ProducerConfig:

    @staticmethod
    def get_producer():
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                 value_serializer=lambda x:
                                 json.dumps(x).encode('utf-8'))
        return producer
