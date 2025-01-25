from fastapi import FastAPI
from fastapi.templating import Jinja2Templates

from mainmenu.main_menu import main_menu as menu
from registration import registration, login

app = FastAPI()
app.include_router(registration.reg_rout)
app.include_router(login.login_rout)

data = {
    "user": {
        "id": 1,
        "name": "<NAME>",
        "money": 5300,
    },
    "products": [{
    "id": 1,
    "name": "Футболка Адидас",
    "price": 3000,
    "description": "Мягкая ткань из хлопка и стильный дизайн популярного бренда!"},
        {
    "id": 2,
    "name": "Штаны Nike",
    "price": 2800,
    "description": "Оригинальный штаны фирмы Nike"},

        ]
    }
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main_menu():
    return templates.TemplateResponse("mainMenu.html", {"request": data})