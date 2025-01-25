from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from models.database.create_databasse import DB_USER, DB_HOST, DB_NAME, DB_PORT, DB_PASSWORD
# Подключение к созданной БД
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Определение модели (таблицы в БД)
class User(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    password = Column(String(100), unique=False, nullable=False)

# Создание таблиц в базе данных
def create_tables():
    Base.metadata.create_all(engine)
    print("Таблицы успешно созданы.")

if __name__ == "__main__":
    create_tables()
