from models.database.create_table import User, SessionLocal, Ticket, Product, Myproducts


def create_user(name, password):
    session = SessionLocal()
    new_user = User(name = name, password = password)
    session.add(new_user)
    session.commit()
    session.close()
    print(f"Пользователь {name} добавлен.")

def get_users(name, password) -> tuple | bool:
    session = SessionLocal()
    users = session.query(User).all()
    for user in users:
        print(user)
        if user.name == name and user.password == password:
            return True, user
    session.close()
    return False

def update_user_money(id: str | int, new_money: float | int) -> bool:
    session = SessionLocal()
    try:
        user = session.query(User).filter_by(id = id).first()
        if user:
            user.money = new_money
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        print(f"Ошибка при обновлении баланса: {e}")
        return False
    finally:
        session.close()

def get_user_info(id) -> tuple | bool:
    session = SessionLocal()
    users = session.query(User).all()
    for user in users:
        if str(user.id) == str(id):
            return user
    session.close()
    return False

def create_ticket(user_id):
    session = SessionLocal()

    products = get_product_in(user_id)[0]
    product_name: str = ''
    for x in products:
        product_name += x.name
        product_name += " "

    new_user = Ticket(product_name = product_name, status = "processing", user_id = user_id)
    print(f'[INFO] New ticket created: {new_user}')

    session.add(new_user)
    session.commit()
    session.close()

    print(f"Тикет {product_name} добавлен")


def get_ticket(id) -> list:
    session = SessionLocal()
    tickets = session.query(Ticket).all()

    tick_id: list = []
    print(f'[USER_ID] {id}')

    for ticket in tickets:
        print(f'[INFO] All id users tickets: {ticket.user_id}')
        if int(ticket.user_id) == int(id):
            tick_id.append(ticket)
    session.close()
    return tick_id


def create_product(name, description, price):
    session = SessionLocal()
    new_user = Product(name = name, description = description, price = price)
    session.add(new_user)
    session.commit()
    session.close()
    print(f"Тикет {name} добавлен")

def get_products():
    session = SessionLocal()
    products = session.query(Product).all()
    prod = []
    for product in products:
        print("Имя: ", product.name)
        prod.append(product)
    session.close()
    return prod

def add_product(id_user, id_product):
    session = SessionLocal()
    new_prod = Myproducts(id_user = id_user, id_product = id_product)
    session.add(new_prod)
    session.commit()
    session.close()
    print(f"Продукт {id_product} добавлен")

def get_cost_product(id_product):
    session = SessionLocal()
    products = session.query(Product).all()
    for product in products:
        if product.id == id_product:
            return product
    print("[INFO] Product is not definded")
    return 0

def get_product_in(id) -> tuple[list, int]:
    session = SessionLocal()
    tickets = session.query(Myproducts).all()

    tick_info: list = []
    total_price: int = 0
    print("[INFO] Starting iterating tickets")

    for ticket in tickets:
        print("[INFO] Products in корзина:", ticket,"ID:", ticket.id_user, id)
        if str(ticket.id_user) == str(id):
            data = get_cost_product(ticket.id_product)
            tick_info.append(data)
            total_price += int(data.price)
    session.close()
    print(f"Tick id: {tick_info}")
    return tick_info, total_price



#Операции для выбора всех(админ панель)

def get_all_users() -> list:
    session = SessionLocal()
    users = session.query(User).all()
    users_all: list = []
    for user in users:
        users_all.append(user)
    session.close()
    return users_all

def get_all_ticket() -> list:
    session = SessionLocal()
    tickets = session.query(Ticket).all()

    tick_id: list = []

    for ticket in tickets:
        tick_id.append(ticket)
    session.close()
    return tick_id

#+get_products но он уже есть, а мы соблюдаем(почти) DRY

def update_user_balance(user_id: int, new_balance: float) -> None:
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    user.money = new_balance
    session.commit()
    session.close()

def update_order_status(id: int, new_status: str) -> None:
    session = SessionLocal()
    ticket = session.query(Ticket).filter(Ticket.id == id).first()
    ticket.status = new_status
    session.commit()
    session.close()


def delete_all_products_by_user(user_id: int) -> None:
    session = SessionLocal()

    # Получаем все товары пользователя
    products = session.query(Myproducts).filter(Myproducts.id_user == user_id).all()

    if products:
        for product in products:
            session.delete(product)
        session.commit()
        print(f"Все товары пользователя с ID {user_id} удалены.")
    else:
        print(f"У пользователя с ID {user_id} нет товаров.")

    session.close()