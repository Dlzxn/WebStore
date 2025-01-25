from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

from models.database.CRUD import get_users
from models.user_models import User

login_rout = APIRouter(prefix="/login")

@login_rout.get("/")
async def login():
    return FileResponse("templates/login.html")

@login_rout.post("/auth")
async def login_post(user: User, responce: Response):
    if get_users(user.username, user.password):
        responce.set_cookie(key = "name", value = user.username)
        return {"status": True}
    else:
        return {"status": False}
