from fastapi import APIRouter, Response
from fastapi.responses import FileResponse
import json

from models.database.CRUD import get_users
from models.user_models import User

login_rout = APIRouter(prefix="/login")

@login_rout.get("/")
async def login():
    return FileResponse("templates/login.html")

@login_rout.post("/auth")
async def login_post(user: User, response: Response):
    if get_users(user.username, user.password):
        data ={
            "user": {
                "username": user.username,
                "money": 5300,
            }
        }
        response.set_cookie(key = "name", value = user.username)
        response.set_cookie(key="money", value=5300)
        return {"status": True}
    else:
        return {"status": False}
