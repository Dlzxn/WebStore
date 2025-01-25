from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
import json

templates = Jinja2Templates(directory="templates")

profile_rout = APIRouter(prefix="/profile")


@profile_rout.get("/")
async def profile(request: Request):
    try:
        print("Cookie:", request.cookies)
        name: str = request.cookies.get("name")
        money: str = request.cookies.get("money")
        if name != None and money != None:
            user_data: dict = {
                "name": name,
                "money": money,
                "orders": [
                    {"id": 1, "product_name": "Laptop", "status": "processing"},
                    {"id": 2, "product_name": "Phone", "status": "delivered"}
                ]
            }
            return templates.TemplateResponse("profile.html", {"request": user_data})
    except Exception as e:
        print(f'[ERROR] {e}')
        print("[INFO] Redirecting user...")
        return RedirectResponse(url="/login")