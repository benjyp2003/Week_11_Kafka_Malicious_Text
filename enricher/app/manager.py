import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

from enricher.app.special_features.find_text_sentiment import find_text_emotion

nltk.download('vader_lexicon')  # Compute sentiment labels
from enricher.app.publisher.pub_kafka_configurations import ProducerConfig

from enricher.app.publisher.pub_kafka_producer import ProducerSet
from enricher.app.special_features.find_relevant_time_stamp import find_relevant_time_stamp
from enricher.app.special_features.find_weapons import check_for_weapons_in_text
from enricher.app.subscriber.sub_kafka_configurations import ConsumerConfig
from enricher.app.weapon_processing.weapons_cleaning import get_clean_weapons


class Manager:
    def __init__(self):
        self.producer = ProducerSet(ProducerConfig())
        self.consumer = ConsumerConfig()
        self.weapons = get_clean_weapons()
        self.sentiment = SentimentIntensityAnalyzer()


    def process_messages(self, topic1, topic2: str):
        try:
            event = self.consumer.get_consumer_events(topic1, topic2)
            for msg in event:
                if msg.topic == topic1:
                    print(msg.value)
                    updated_data = self.update_docs(msg.value)
                    print(updated_data)
                    self.producer.publish_message("enriched_preprocessed_tweets_antisemitic", updated_data)

                elif msg.topic == topic2:
                    print(msg.value)
                    updated_data = self.update_docs(msg.value)
                    print(updated_data)
                    self.producer.publish_message("enriched_preprocessed_tweets_not_antisemitic", updated_data)
        except Exception as e:
            raise Exception(f"Error processing messages: {e}")

    def update_docs(self, docs: list[dict]):
        try:
            updated_docs = docs.copy()
            print(updated_docs)
            for doc in updated_docs:
                text = doc["clean_text"]
                found_weapons = check_for_weapons_in_text(text, self.weapons.split())
                doc["weapons_detected"] = found_weapons
                doc["relevant_timestamp"] = find_relevant_time_stamp(text)
                doc["sentiment"] = find_text_emotion(text, self.sentiment)
            print(updated_docs)
            return updated_docs
        except Exception as e:
            raise Exception(f"Error updating document: {e}")





if __name__ == "__main__":
    manager = Manager()
    manager.process_messages("preprocessed_tweets_antisemitic","preprocessed_tweets_not_antisemitic")


