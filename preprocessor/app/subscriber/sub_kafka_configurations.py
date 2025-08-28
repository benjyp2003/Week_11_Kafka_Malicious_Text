from kafka import KafkaConsumer
import json

class ConsumerConfig:

    @staticmethod
    def get_consumer_events(topic1,topic2):

        consumer = KafkaConsumer(topic1,topic2,
                                 group_id='my-group',
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')),
                                 bootstrap_servers=['localhost:9092'])

        return consumer
