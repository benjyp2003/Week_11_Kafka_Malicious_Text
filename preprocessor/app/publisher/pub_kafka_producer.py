# from pub_kafka_configurations import ProducerConfig

class ProducerSet:
    def __init__(self,producer_config ):
        self.producer_con = producer_config
        self.producer = self.producer_con.get_producer()


    def publish_message(self,topic,message):
        self.producer.send(topic, message)


# if __name__ == '__main__':
#     producer_set = ProducerSet(ProducerConfig())
#     #"enriched_preprocessed_tweets_antisemitic"
#     #"enriched_preprocessed_tweets_not_antisemitic"
#
#
#     # logging.info("Producer metrics", producer.metrics())
#     event = {"App": "Producer 1"}

    # producer_set.publish_message( "topic1", event)
    #
    # producer_set.producer.flush()