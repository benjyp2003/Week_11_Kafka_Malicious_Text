#from sub_kafka_configurations import ConsumerConfig


class ConsumerSet:
    def __init__(self,consumer_config,topic):
        self.topic = topic
        self.consumer_con = consumer_config
        self.events = self.consumer_con.get_consumer_events(self.topic)


    def print_messages(self):
        for message in self.events:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key,
                                                 message.value))
    def get_messages_in_list(self):
        for message in self.events:
            return message.value

# if __name__ == '__main__':
#     consumer_antisemitic = ConsumerSet(ConsumerConfig(),"raw_tweets_antisemitic")
#     #consumer_antisemitic.print_messages()
#     print(consumer_antisemitic.get_messages_in_list())
#     consumer_not_antisemitic = ConsumerSet(ConsumerConfig(), "raw_tweets_not_antisemitic")
#     #consumer_not_antisemitic.print_messages()
#     print(consumer_not_antisemitic.get_messages_in_list())
