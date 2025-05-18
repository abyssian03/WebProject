from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

from app.models.models import Product


app = FastAPI()

first_product = {"name": "potato", "price": 2}
my_product = Product(**first_product)


@app.get("/index")
async def index():
    return FileResponse("index.html")


@app.post("/index")
async def index(name: str = Form(), price: int = Form()):
    second_product = {"name": name, "price": price}
    if second_product == first_product:
        return {"message": "Такой товар уже есть!"}
    else:
        your_product = Product(**second_product)
        return {"name": your_product.name, "price": your_product.price}


@app.get("/product")
async def get_product():
    return my_product


@app.get("/")
async def index():
    return {"message": "Добро пожаловать в магазин!"}
