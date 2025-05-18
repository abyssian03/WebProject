import logging

from fastapi import FastAPI
from pydantic import BaseModel

from app.config import load_config


app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    logger.info("Handling request to root endpoint")
    return {"message": "Hello, World!"}


class User(BaseModel):
    username: str
    message: str


@app.post("/")
async def root(user: User):
    """ """
    print(f"Мы получили от юзера {user.username} такое сообщение: {user.message}")
    return user


config = load_config()

if config.debug:
    app.debug = True
else:
    app.debug = False
