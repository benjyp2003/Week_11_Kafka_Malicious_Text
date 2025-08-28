class ProducerSet:
    def __init__(self,producer_config ):
        self.producer_con = producer_config
        self.producer = self.producer_con.get_producer()


    def publish_message(self,topic,message):
        self.producer.send(topic, message)

