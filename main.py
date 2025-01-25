from fastapi import FastAPI, Request, Response
from fastapi.params import Cookie
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


from registration import registration, login
from profile import profile_user
from models.database.CRUD import get_products
from myproducts import pay

app = FastAPI()
app.include_router(registration.reg_rout)
app.include_router(login.login_rout)

app.include_router(profile_user.profile_rout)

app.include_router(pay.pay_rout)


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
async def main_menu(request: Request):
    try:
        print("Cookie:", request.cookies)
        name: str = request.cookies.get("name")
        money: str = request.cookies.get("money")
        id_user: str = request.cookies.get("id")
        print("[INFO] User going to Main Menu")

        data = create_data(name, money, id_user)
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