from classifier import Classifier
from dal import Dal
from kafka_producer import Producer


class Manager:
    def __init__(self,producer:Producer):
        self.producer = producer
        self.dal = Dal("tweets")
        self.classifier = Classifier()

    def publish_messages(self):
        try:
            docs = self.dal.fetch_100_latest_docs()
            classified_docs = self.classifier.classify_docs(docs)
            self.producer.publish("raw_tweets_antisemitic", classified_docs.get("antisemitic"))
            print("Published antisemitic tweets successfully.")
            self.producer.publish("raw_tweets_not_antisemitic", classified_docs.get("not_antisemitic"))
            print("Published not antisemitic tweets successfully.")
            self.producer.flush()

        except Exception as e:
            raise Exception(f"Error publishing messages: {e}")


