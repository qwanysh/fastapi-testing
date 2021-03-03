from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get('/hello-world')
async def hello_world():
    return PlainTextResponse('Hello, world!')


@app.get('/{number}')
async def get_number(number: int):
    return {'number': number}
