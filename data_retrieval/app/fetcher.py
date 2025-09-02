from pymongo import MongoClient
class Connector:
    def __init__(self, uri="mongodb://mongodb:27017/", db_name="tweets"):
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