from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from models.database.CRUD import get_ticket


templates = Jinja2Templates(directory="templates")

profile_rout = APIRouter(prefix="/profile")


@profile_rout.get("/")
async def profile(request: Request):
    try:
        print("Cookie:", request.cookies)
        name: str = request.cookies.get("name")
        money: str = request.cookies.get("money")
        id: str = request.cookies.get("id")
        if name != None and money != None:
            my_ticket = get_ticket(id)
            print(f"[INFO] My Ticket:{my_ticket}")
            user_data: dict = {
                "name": name,
                "money": money,
                "orders": [{"id": x.id, "product_name": x.product_name, "status": x.status} for x in my_ticket]
            }
            return templates.TemplateResponse("profile.html", {"request": user_data})

    except Exception as e:
        print(f'[ERROR] {e}')
        print("[INFO] Redirecting user...")
        return RedirectResponse(url="/login")
