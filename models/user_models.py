from pydantic import BaseModel

class User(BaseModel):
    """

    """
    username: str
    password: str

class UserBase(BaseModel):
    name: str
    money: int

class AddProducts(BaseModel):
    product_id: str
    user_id: str


class PayAll(BaseModel):
    user_id: str | int | float
    total_price: int | str

class AddProduct(BaseModel):
    name: str
    description: str
    price: int | str

class UpdateUser(BaseModel):
    id: str | int | float
    balance: int | str

class UpdateStatus(BaseModel):
    id: str | int | float
    status: str
