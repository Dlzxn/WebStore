from fastapi import FastAPI, Request, Response
from fastapi.params import Cookie
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

import admin
from registration import registration, login
from profile import profile_user
from models.database.CRUD import get_products, get_user_info
from myproducts import pay
from admin import admin_panel

app = FastAPI()
app.include_router(registration.reg_rout)
app.include_router(login.login_rout)

app.include_router(profile_user.profile_rout)

app.include_router(pay.pay_rout)

app.include_router(admin_panel.adm_rout)


templates = Jinja2Templates(directory="templates")
def create_data(name: str, money: int | str, id_user: str) -> dict:
    print("[INFO]- ", name)
    data = {
    "user": {
        "name": name,
        "money": money,
        "id": id_user
    },
    "products": [{"id": x.id, "name": x.name, "price": x.price, "description": x.description} for x in get_products()]
    }
    return data

@app.get("/")
async def main_menu(request: Request, response: Response):
    try:
        print("Cookie:", request.cookies)
        name: str = request.cookies.get("name")
        money: str = request.cookies.get("money")
        id_user: str = request.cookies.get("id")
        print("[INFO] User going to Main Menu")
        data = get_user_info(id_user)
        print(f"[INFO] User info money: {data.money}")
        if data:
            response.delete_cookie("money")
            response.set_cookie(key="money", value=data.money)
            response.set_cookie(key="id", value=data.id)

        data = create_data(name, data.money, id_user)
        return templates.TemplateResponse("mainMenu.html", {"request": data})

    except Exception as e:
        print(f'[ERROR] Main {e}')
        print("[INFO] Redirecting user to login page")
        return RedirectResponse(url = "/login")

@app.get("/exit")
async def exit_login(response: Response):
    response.delete_cookie("name")
    response.delete_cookie("money")
    response.delete_cookie("data")
    return RedirectResponse(url = "/login")