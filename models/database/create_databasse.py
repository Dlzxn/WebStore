from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import os

load_dotenv() #загрузка .env

# Указываем параметры подключения (без указания конкретной БД)
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Формируем строку подключения
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создание движка без указания базы данных для создания самой БД
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres")

# Проверка существования базы данных и её создание
if not database_exists(DATABASE_URL):
    create_database(DATABASE_URL)
    print(f"База данных '{DB_NAME}' успешно создана.")
else:
    print(f"База данных '{DB_NAME}' уже существует.")
