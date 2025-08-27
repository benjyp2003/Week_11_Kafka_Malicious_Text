from subscriber.sub_kafka_consumer import ConsumerSet
from subscriber.sub_kafka_configurations import ConsumerConfig
class Manager:
    def __init__(self):
        self.consumer_antisemitic = ConsumerSet(ConsumerConfig(),"raw_tweets_antisemitic")
        self.antisemitic_list = self.consumer_antisemitic.get_messages_in_list()
        self.consumer_not_antisemitic = ConsumerSet(ConsumerConfig(), "raw_tweets_not_antisemitic")
        self.not_antisemitic_list = self.consumer_not_antisemitic.get_messages_in_list()


if __name__ == "__main__":
    manager = Manager()
    print(manager.antisemitic_list)
    print(manager.not_antisemitic_list)