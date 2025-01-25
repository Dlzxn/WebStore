from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.database.CRUD import get_ticket, add_product, get_product_in, get_user_info, update_user_money
from models.user_models import AddProduct, PayAll

pay_rout = APIRouter(prefix="/myproducts")

templates = Jinja2Templates(directory="templates")

@pay_rout.get("/")
async def get_pay(request: Request):
    print(f"Вы в разделе корзина")
    try:
        name = request.cookies.get("name")
        money = request.cookies.get("money")
        id = request.cookies.get("id")
        tickets, total_price = get_product_in(id)
        data = {
            "name": name,
            "money": money,
            "tickets": tickets,
            "total_price": total_price,
            "id": id,
        }
        return templates.TemplateResponse("myproducts.html", {"request": data})

    except Exception as e:
        print(f"[ERROR] {e}")
        return RedirectResponse(url="/")

@pay_rout.post("/add")
async def pay_add(data: AddProduct):
    print(f"[INFO] Add product: {data}")
    add_product(data.user_id, data.product_id)
    return {"status": True}

@pay_rout.post("/start")
async def pay_start(data: PayAll):
    print(f"[INFO] PayAll: {data}")
    try:
        user = get_user_info(data.user_id) #получаем данные из бд
        if user:
            if  user.money>= int(data.total_price):
                update_user_money(data.user_id, user.money - data.total_price) #обновление денег в бд

                return {"status": True}
            else:
                return {"status": False}
        else:
            return {"status": False}

    except Exception as e:
        print(f"[ERROR] {e}")
        return {"status": False}