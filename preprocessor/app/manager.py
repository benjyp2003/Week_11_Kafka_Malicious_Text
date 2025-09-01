from publisher.pub_kafka_producer import ProducerSet
from publisher.pub_kafka_configurations import ProducerConfig
from update_data import Update
from time import time

class Manager:
    def __init__(self):
        self.consumer = ConsumerConfig()
        self.producer = ProducerSet(ProducerConfig())

    def process_messages(self, topic1, topic2: str):
        try:
            event = self.consumer.get_consumer_events(topic1, topic2)
            for msg in event:
                if msg.topic == topic1:
                    print(msg.value)
                    update = Update(msg.value)
                    new_data = update.clean_and_update_text()

                    self.producer.publish_message("preprocessed_tweets_antisemitic",new_data)

                elif msg.topic == topic2:
                    update = Update(msg.value)
                    new_data = update.clean_and_update_text()

                    self.producer.publish_message("preprocessed_tweets_not_antisemitic", new_data)
        except Exception as e:
                raise Exception(f"Error consuming messages from topic {topic1} and {topic2}: {e}")






if __name__ == "__main__":
    manager = Manager()
    manager.process_messages("raw_tweets_antisemitic", "raw_tweets_not_antisemitic")
