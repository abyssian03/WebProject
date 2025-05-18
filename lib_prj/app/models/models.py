from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: int

class User(BaseModel):
    username: str
    user_info: str
