from fastapi import FastAPI
from pydantic.v1 import BaseModel

from manager import Manager
man = Manager()


app = FastAPI()
class TweetRespons(BaseModel):
    tweets: list[dict]

@app.get('/check')
def app1():
    return  "hellooooooooo"

@app.get("/antic",response_model=TweetRespons)
def get_antic():
    return  man.get_tweets_antisemitic()

@app.get("/not_antic",response_model=TweetRespons)
def get_antic():
    return man.get_tweets_not_antisemitic()
