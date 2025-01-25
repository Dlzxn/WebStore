from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# Указываем параметры подключения (без указания конкретной БД)
DB_USER = "myuser"
DB_PASSWORD = "mypassword"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "mydatabase"

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
