from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from manager import Manager
man = Manager()


app = FastAPI()
class TweetResponse(BaseModel):
    tweets: list[dict]

@app.get('/')
async def app1():
    return  {"message":"Welcome to the Antisemitic Tweet analyzer API",
             "endpoints": " /get_antisemitic to get antisemitic tweets and /get_not_antisemitic to get non-antisemitic tweets"}

@app.get("/get_antisemitic",response_model=TweetResponse)
async def get_antic():
    tweets = man.get_tweets_antisemitic()
    payload = {"tweets": tweets}
    return JSONResponse(
        content=jsonable_encoder(payload, custom_encoder={ObjectId: str})
    )

@app.get("/get_not_antisemitic",response_model=TweetResponse)
async def get_antic():
    tweets = man.get_tweets_not_antisemitic()
    payload = {"tweets": tweets}
    return JSONResponse(
        content=jsonable_encoder(payload, custom_encoder={ObjectId: str})
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)