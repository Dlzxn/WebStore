<!--
 ██████╗ ███████╗██████╗ ███████╗████████╗███████╗
██╔════╝ ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝
██║  ███╗█████╗  ██████╔╝███████╗   ██║   █████╗  
██║   ██║██╔══╝  ██╔══██╗╚════██║   ██║   ██╔══╝  
╚██████╔╝███████╗██║  ██║███████║   ██║   ███████╗
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝
-->

<p align="center">
  <img src="https://i.imgur.com/Jyod8Dh.gif" width="80" height="80" />
</p>

# 🚀 WebStore | FastAPI + PostgreSQL

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-0.100-green?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/PostgreSQL-14-blue?style=for-the-badge&logo=postgresql" />
</p>

---

## 🎯 Описание проекта

**WebStore** — это современный интернет-магазин, разработанный с использованием **FastAPI** для серверной части и **PostgreSQL** для хранения данных. Интерфейс сайта выполнен в минималистичном стиле с адаптивным дизайном.

### ⚡ Ключевые особенности проекта:
- 📦 **Управление товарами:** Полный набор CRUD-операций.
- 🛒 **Корзина и заказы:** Добавление товаров в корзину и отслеживание статуса заказов.
- 👤 **Авторизация:** Регистрация и управление профилем.
- ⚙️ **Админ-панель:** Управление товарами, пользователями и заказами.
- 📊 **База данных:** PostgreSQL с SQLAlchemy.
- 🔒 **Безопасность:** Хеширование паролей и защита CSRF.

---

## 🚀 Установка и запуск

1. **Клонирование репозитория:**
```bash
git clone https://github.com/Dlzxn/WebStore.git
cd WebStore
```

2. **Создание и активация виртуального окружения:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. **Установка зависимостей:**
```bash
pip install -r requirements.txt
```

4. **Настройка переменных окружения:**
Создайте `.env` файл:
```env
DB_HOST=your_database_host
DB_PORT=5432
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
SECRET_KEY=your_secret_key
```

5. **Применение миграций:**
```bash
alembic upgrade head
```

6. **Запуск проекта:**
```bash
uvicorn main:app --reload
```

Приложение будет доступно по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠️ Используемые технологии

- **FastAPI** — быстрый и асинхронный фреймворк для Python.
- **PostgreSQL** — реляционная база данных.
- **SQLAlchemy** — ORM для работы с базой данных.
- **Jinja2** — шаблонизатор для рендеринга HTML.
- **HTML/CSS/JS** — фронтенд.
- **Alembic** — управление миграциями базы данных.

---

## 📂 Структура проекта

```
📦 WebStore
├── 📂 admin
├── 📂 mainmenu
├── 📂 models
├── 📂 myproducts
├── 📂 profile
├── 📂 registration
├── 📂 user
├── 📂 templates
│   ├── admin/
│   ├── mainmenu/
│   ├── myproducts/
│   ├── profile/
│   ├── registration/
│   ├── user/
│   ├── base.html
│   ├── index.html
└── main.py
```

---

## 🔗 Основные маршруты

| HTTP Метод | Маршрут         | Описание                  |
|------------|----------------|---------------------------|
| GET        | `/`             | Главная страница           |
| POST       | `/auth/login`   | Авторизация пользователя   |
| POST       | `/auth/register`| Регистрация пользователя   |
| GET        | `/products`     | Список товаров             |
| POST       | `/cart/add`     | Добавление в корзину        |

---

<p align="center"><i>Спасибо за использование нашего проекта!</i></p>

