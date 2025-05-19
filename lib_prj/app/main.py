import logging

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

from app.models.models import User, Feedback

#from app.config import load_config


app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


fake_db = {1: {"username": "vasya", "user_info": "любит колбасу"}, 2: {"username": "katya", "user_info": "любит петь"}}



# Получение списка пользователей с параметрами
@app.get('/users')
async def get_users(username: str = '', limit: int = 10):
    filtered_users = fake_users

    filtered_users = {key: user for key, user in filtered_users.items() if username.lower() in user["username"].lower()}

    return dict(list(filtered_users.items())[:limit])


#Вывод формы для добавления пользователя
@app.get("/add")
async def add_user():
    return FileResponse("add_user.html")


# Добавление нового пользователя (параметр тела запроса)
@app.post("/add")
async def add_user(name: str = Form(), info: str = Form()):
    new_user = {"username": name, "user_info": info}
    for key in fake_db:
        if new_user == fake_db[key]:
            return {"message": "Такой пользователь уже есть!"}
        else:
            your_user = User(**new_user)
            fake_db.update({len(fake_db)+1: your_user})
            return {"message": "Пользователь добавлен!"}

#Получение фидбэка
@app.post("/feedback")
async def get_feedback(data: Feedback):
     for key in fake_db:
         if data.username == fake_db[key]["username"]:
             return {"message": f"Спасибо за отзыв, {data.username}!"}
     return {"message": f"Пользователь {data.username} не зарегистрирован!"}

#Вывод сообщения о входе c параметром
@app.get("/{username}")
async def greeting(username: str):
    return {"message": f"Добро пожаловать, {username}!"}


#Вывод сообщения о входе в root
@app.get("/")
async def root():
    return {"message": "Добро пожаловать!"}


#config = load_config()

# if config.debug:
#     app.debug = True
# else:
#     app.debug = False
