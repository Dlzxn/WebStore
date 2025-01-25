from pydantic import BaseModel

class User(BaseModel):
    """

    """
    username: str
    password: str

class UserBase(BaseModel):
    name: str
    money: int

class AddProduct(BaseModel):
    product_id: str | int | float
    user_id: str | int | float


class PayAll(BaseModel):
    user_id: str | int | float
    total_price: int | str