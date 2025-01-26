from fastapi import APIRouter, Response
from fastapi.responses import FileResponse


from models.database.CRUD import get_users
from models.user_models import User

login_rout = APIRouter(prefix="/login")

@login_rout.get("/")
async def login():
    return FileResponse("templates/login.html")

@login_rout.post("/auth")
async def login_post(user: User, response: Response):
    try:
        data = get_users(user.username, user.password)
        print("[INFO] Data: ", data[1].id)
        if data:
            response.set_cookie(key = "name", value = user.username)
            response.set_cookie(key="money", value = data[1].money)
            response.set_cookie(key = "id", value = data[1].id)
            return {"status": True}
        else:
            return {"status": False}
    except Exception as e:
        print(f"[ERROR] Login err - {e}")
        return {"status": False}
