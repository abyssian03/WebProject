import logging

from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

from app.models.models import User, Feedback

#from app.config import load_config


app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

user1 = User(username = "vasya", user_info = "любит колбасу")
user2 = User(username = "katya", user_info = "любит петь")

fake_db = [user1, user2]



# Получение списка пользователей с параметрами
@app.get('/users')
async def get_users(username: str = '', limit: int = 10):
    filtered_users = [user for user in fake_db if username.lower() in user.username.lower()]

    return filtered_users[:limit]


#Вывод формы для добавления пользователя
@app.get("/add")
async def add_user():
    return FileResponse("add_user.html")


# Добавление нового пользователя (параметр тела запроса)
@app.post("/add")
async def add_user(name: str = Form(), info: str = Form()):
    new_user = User(username = name, user_info = info)
    if new_user in fake_db:
        return {"message": "Такой пользователь уже есть!"}
    else:
        fake_db.append(new_user)
        return {"message": "Пользователь добавлен!"}


#Вывод формы для добавления отзыва
@app.get("/feedback")
async def add_feedback():
    return FileResponse("add_feedback.html")


# Добавление отзыва
@app.post("/feedback")
async def add_feedback(name: str = Form(), message: str = Form()):
    new_feedback = Feedback(username = name, message = message)
    for user in fake_db:
        if new_feedback.username == user.username:
            return {"message": f"Спасибо за отзыв, {name}!"}
    return {"message": "Зарегистрируйтесь в базе, чтобы оставить отзыв"}


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
