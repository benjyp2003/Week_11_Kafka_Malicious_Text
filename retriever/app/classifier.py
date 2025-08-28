
class Classifier:

    def classify_docs(self, document) -> dict:
        """Classifies documents into antisemitic and not antisemitic based on the 'Antisemitic' field."""
        try:
            raw_tweets_antisemitic, raw_tweets_not_antisemitic = [], []
            for doc in document:
                is_antisemitic = not doc.get("Antisemitic")
                if is_antisemitic:
                    raw_tweets_antisemitic.append(doc)
                else:
                    raw_tweets_not_antisemitic.append(doc)

            return {"antisemitic": raw_tweets_antisemitic, "not_antisemitic": raw_tweets_not_antisemitic}


        except Exception as e:
            raise Exception(f"Error classifying document: {e}")


