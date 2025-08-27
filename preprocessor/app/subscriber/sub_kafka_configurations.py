from kafka import KafkaConsumer
import json

class ConsumerConfig:

    @staticmethod
    def get_consumer_events(topic):

        consumer = KafkaConsumer(topic,
                                 group_id='my-group',
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=['localhost:9092'],
                                 consumer_timeout_ms=10000)
        return consumer
