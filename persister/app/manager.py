from dal import Dal
from subscriber.sub_kafka_configurations import ConsumerConfig



class Manager:
    def __init__(self):
        self.consumer = ConsumerConfig()
        self.dal = Dal()

    def process_messages(self, topic1, topic2: str):
        try:
            event = self.consumer.get_consumer_events(topic1, topic2)
            for msg in event:
                if msg.topic == topic1:
                    self.dal.insert_docs(msg.value, "tweets_antisemitic")

                elif msg.topic == topic2:
                    self.dal.insert_docs(msg.value, "tweets_not_antisemitic")
        except Exception as e:
                raise Exception(f"Error consuming messages from topic {topic1} and {topic2}: {e}")






if __name__ == "__main__":
    manager = Manager()
    manager.process_messages("enriched_preprocessed_tweets_not_antisemitic", "enriched_preprocessed_tweets_antisemitic")
