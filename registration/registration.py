from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

from models.user_models import User
from models.database import CRUD as Model

reg_rout = APIRouter(prefix="/registration")

@reg_rout.get("/")
async def registration():
    return FileResponse("templates/registration.html")

@reg_rout.post("/base")
async def registration_base(user: User):
    print(user)
    try:
        Model.create_user(user.username, user.password)
        return {"status": True}
    except Exception as e:
        print(e)
        return {"status": False, "message": str(e)}

