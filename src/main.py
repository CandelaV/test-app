from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from log_middleware import LogMiddleware
from random import randrange
import logging

logger = logging.getLogger()


app = FastAPI(
    title="Test Monitoring FastAPI"
)

app.add_middleware(LogMiddleware)

Instrumentator().instrument(app).expose(app)


@app.get("/")
async def root():
    logger.warn("Hello World.")
    return {"message": "Hello Universe!!"}


@app.get("/random")
async def random_generator():
    some_value = randrange(10)
    logger.warn("Value generated.", extra={"some_value": some_value})
    return {"message": "Random value: {}".format(some_value)}
