from pydantic import BaseModel

class User(BaseModel):
    """

    """
    username: str
    password: str

class UserBase(BaseModel):
    name: str
    money: int