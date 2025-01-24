from fastapi import APIRouter
from fastapi.responses import FileResponse

main_menu = APIRouter()

@main_menu.get("/")
async def main_menu():
    return FileResponse("main/templates/mainMenu.html")