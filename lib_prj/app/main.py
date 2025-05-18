import logging

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

from app.models.models import User

#from app.config import load_config


app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


fake_db = [{"username": "vasya", "user_info": "любит колбасу"}, {"username": "katya", "user_info": "любит петь"}]

@app.get("/")
async def root():
    return {"message": "Добро пожаловать!"}

@app.get("/add")
async def index():
    return FileResponse("index.html")

@app.get('/users')
async def get_all_users():
    return fake_db

@app.post("/add")
async def index(name: str = Form(), info: str = Form()):
    new_user = {"username": name, "user_info": info}
    if new_user in fake_db:
        return {"message": "Такой пользователь уже есть!"}
    else:
        your_user = User(**new_user)
        fake_db.append(your_user)
        return {"message": "Пользователь добавлен!"}

#config = load_config()

# if config.debug:
#     app.debug = True
# else:
#     app.debug = False
