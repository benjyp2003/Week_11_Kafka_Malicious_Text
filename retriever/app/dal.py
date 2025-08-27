import os
from pymongo import MongoClient, errors


class Dal:
    def __init__(self, collection_name):
        self.db = None
        self.user = os.getenv("MONGO_USER", "IRGC_NEW")
        self.password = os.getenv("MONGO_PASSWORD", "iran135")
        self.database_name = os.getenv("MONGO_DATABASE", "IranMalDB")
        self.uri = f"mongodb+srv://{self.user}:{self.password}@{self.database_name}cluster0.6ycjkak.mongodb.net/"
        self.collection_name = collection_name
        self.counter = 0 # a counter to keep track of the number of documents fetched so far


    def fetch_100_latest_docs(self):
        """ Fetch all documents from a MongoDB collection."""
        try:
            with MongoClient(self.uri) as client:
                self.db = client[self.database_name]
                collection = self.db[self.collection_name]
                result = list(collection.find().sort({ 'CreateDate': 1 }).skip(self.counter).limit(100))
                self.counter += 100
                return result

        except errors.PyMongoError as e:
            raise Exception(f"Error fetching docs from {collection} collection: {e}")




