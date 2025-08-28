from fetcher import Connector
class Manager:
    def __init__(self):
        self.connector = Connector()
        self.db = self.connector.get_db()
        self.tweets_antisemitic = self.db["tweets_antisemitic"]
        self.tweets_not_antisemitic = self.db["tweets_not_antisemitic"]

    def get_tweets_antisemitic(self):
        return list(self.tweets_antisemitic.find())


    def get_tweets_not_antisemitic(self):
        return list(self.tweets_not_antisemitic.find())
