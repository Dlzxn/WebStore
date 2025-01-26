from fastapi import APIRouter, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from models.database.CRUD import (get_user_info, get_all_users, get_all_ticket, get_products, create_product,
                                  update_user_balance, update_order_status)
from models.user_models import AddProduct, UpdateUser, UpdateStatus

adm_rout = APIRouter(prefix = "/admin") #устанаваливаем путь админ панели

templates = Jinja2Templates("templates") #устанавливаем папку для шаблонов HTML

@adm_rout.get("/")
async def admin_home(request: Request):
    id: int | str = request.cookies.get("id")
    user_info = get_user_info(id)
    try:
        print(f'[INFO] User: {user_info}')
        if user_info.super_user:
            products = get_products()
            tickets = get_all_ticket()
            users = get_all_users()

            data = {
                "products": products,
                "tickets": tickets,
                "users": users,
            }
            return templates.TemplateResponse("admin.html", {"request": data})
        else:
            return RedirectResponse("/")

    except Exception as er:
        print(f"[ERROR] Error Admin Panel: {er}")
        return RedirectResponse("/")

@adm_rout.post("/add_product")
async def add_product(data: AddProduct):
    try:
        create_product(data.name, data.description, data.price)
        return {"status": True}
    except Exception as er:
        print(f"[ERROR] Error Dont add product in base: {er}")


@adm_rout.post("/update_user")
async def update_user(data: UpdateUser):
    try:
        update_user_balance(data.id, data.balance)
        return {"status": True}
    except Exception as er:
        print(f"[ERROR] Error Dont update user: {er}")
        return {"status": False}

@adm_rout.post("/update_ticket_status")
async def update_status(data: UpdateStatus):
    try:
        update_order_status(data.id, data.status)
        return {"status": True}
    except Exception as er:
        print(f"[ERROR] Error Dont update status: {er}")
        return {"status": False}

#все пост запросы посредственные, они фоново вызываются при нажатии на кнопку, в данном случае кнопки в админ меню
