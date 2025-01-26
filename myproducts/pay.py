from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.database.CRUD import (get_ticket, add_product, get_product_in, get_user_info, update_user_money, create_ticket,
                                  delete_all_products_by_user)
from models.user_models import AddProducts, PayAll

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
async def pay_add(data: AddProducts):
    """
    Функция, которой передаются данные для занесения в бд
    через нее проходит добавление в корзину самих товаров
    :param data:
    :return:
    """
    print(f"[INFO] Add product: {data}")
    add_product(data.user_id, data.product_id)
    return {"status": True}

@pay_rout.post("/start")
async def pay_start(data: PayAll):
    """
    эта функция получает пост запрос когда мы нажимаем оплатиь, проверяются все нужные условия
    снимаются деньги и после этого создается заказ
    :param data:
    :return:
    """
    print(f"[INFO] PayAll: {data}")
    try:
        user = get_user_info(data.user_id) #получаем данные из бд
        if user:
            if  user.money >= int(data.total_price):
                print(f'[INFO] User payed ticket: {data}')
                update_user_money(data.user_id, user.money - data.total_price) #обновление денег в бд
                create_ticket(data.user_id)
                delete_all_products_by_user(data.user_id)

                return {"status": True}
            else:
                print(f'[ERROR] User dont payed ticket: {data}')
                return {"status": False}
        else:
            print(f'[ERROR] User dont payed ticket: {data}')
            return {"status": False}

    except Exception as e:
        print(f"[ERROR] {e}")
        return {"status": False}


#P.S. По факту дела, это не функции, а корутины, если говорить правильно