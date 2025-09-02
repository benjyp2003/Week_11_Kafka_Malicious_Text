import os

from pymongo import MongoClient, errors


class Dal:
    def __init__(self):
        self.client = None
        self.db = None
        self.database_name = os.getenv("MONGO_DB_NAME", "tweets")
        self.mongo_host = os.getenv("MONGO_HOST", "localhost")
        self.mongo_port = os.getenv("MONGO_PORT", "27017")
        self.uri = f"mongodb://{self.mongo_host}:{self.mongo_port}/"


    def insert_docs(self, docs, collection_name: str):
        try:
             # Add validation for empty docs
            if not docs or len(docs) == 0:
                print(f"Warning: Received empty document list for collection {collection_name}")
                return
                
            with MongoClient(self.uri) as client:
                self.db = client[self.database_name]
                collection = self.db[collection_name]
                collection.insert_many(docs)

        except errors.PyMongoError as e:
            raise Exception(f"Error inserting docs into {collection} collection: {e}")
        except Exception as e:
            raise Exception(f"Error inserting docs into {collection} collection: {e}")