from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse


from registration import registration, login
from profile import profile_user
from models.database.CRUD import get_products

app = FastAPI()
app.include_router(registration.reg_rout)
app.include_router(login.login_rout)

app.include_router(profile_user.profile_rout)


templates = Jinja2Templates(directory="templates")
def create_data(name: str, money: int | str) -> dict:
    print("[INFO]- ", name)
    data = {
    "user": {
        "name": name,
        "money": money,
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
        print("[INFO] User going to Main Menu")

        data = create_data(name, money)
        return templates.TemplateResponse("mainMenu.html", {"request": data})

    except Exception as e:
        print(f'[ERROR] {e}')
        print("[INFO] Redirecting user to login page")
        return RedirectResponse(url = "/login")