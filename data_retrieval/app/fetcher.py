from pymongo import MongoClient
import os

class Connector:
    def __init__(self, uri=None, db_name="tweets"):
        if uri is None:
            # Use environment variable or default to Docker container name
            mongo_host = os.getenv('MONGO_HOST', 'mongodb')
            mongo_port = os.getenv('MONGO_PORT', '27017')
            uri = f"mongodb://{mongo_host}:{mongo_port}/"
        self.uri = uri
        self.client = MongoClient(self.uri)
        self.db = self.client[db_name]


    def get_db(self):
        return self.db

    def close(self):
        self.client.close()

if __name__ == "__main__":
    con = Connector()

    db = con.get_db()
    tweets_antisemitic = db["tweets_antisemitic"]
    tweets_not_antisemitic = db["tweets_not_antisemitic"]

    for r in tweets_antisemitic.find():
        print(r)
    for r in tweets_not_antisemitic.find():
        print(r)

    con.close()