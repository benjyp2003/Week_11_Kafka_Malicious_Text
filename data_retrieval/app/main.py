import uvicorn
from bson import ObjectId
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
import uvicorn
from starlette.responses import JSONResponse

from manager import Manager
man = Manager()


app = FastAPI()
class TweetRespons(BaseModel):
    tweets: list[dict]

@app.get('/check')
async def app1():
    return  "hellooooooooo"

@app.get("/antic",response_model=TweetRespons)
async def get_antic():
    tweets = man.get_tweets_antisemitic()
    payload = {"tweets": tweets }
    return JSONResponse(
        content=jsonable_encoder(payload, custom_encoder={ObjectId: str})
    )

@app.get("/not_antic",response_model=TweetRespons)
async def get_not_antic():
    tweets = man.get_tweets_not_antisemitic()
    payload = {"tweets": tweets}
    return JSONResponse(
        content=jsonable_encoder(payload, custom_encoder={ObjectId: str})
    )
if __name__ == "__main__":
    uvicorn.run(app,host = "0.0.0.0",port = 8082)