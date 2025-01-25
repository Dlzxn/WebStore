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
        if user.id == id:
            return user
    session.close()
    return False

def create_ticket(product_name, status, user_id):
    session = SessionLocal()
    new_user = Ticket(product_name = product_name, status = status, user_id = user_id)
    session.add(new_user)
    session.commit()
    session.close()
    print(f"Тикет {product_name} добавлен")

def get_ticket(id) -> tuple[list, int]:
    session = SessionLocal()
    tickets = session.query(Ticket).all()

    tick_id: list = []
    total_price: int = 0

    for ticket in tickets:
        print(ticket)
        if ticket.id == id:
            tick_id.append(ticket.id)
            total_price += int(ticket.price)
    session.close()
    return tick_id, total_price

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


