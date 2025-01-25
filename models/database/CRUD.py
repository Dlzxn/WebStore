from models.database.create_table import User, SessionLocal, Ticket, Product

def create_user(name, password):
    session = SessionLocal()
    new_user = User(name = name, password = password)
    session.add(new_user)
    session.commit()
    session.close()
    print(f"Пользователь {name} добавлен.")

def get_users(name, password):
    session = SessionLocal()
    users = session.query(User).all()
    for user in users:
        print(user)
        if user.name == name and user.password == password:
            return True
    session.close()
    return False

def create_ticket(product_name, status, user_id):
    session = SessionLocal()
    new_user = Ticket(product_name = product_name, status = status, user_id = user_id)
    session.add(new_user)
    session.commit()
    session.close()
    print(f"Тикет {product_name} добавлен")

def get_ticket(id):
    session = SessionLocal()
    tickets = session.query(Ticket).all()
    for ticket in tickets:
        print(ticket)
        if ticket.id == id:
            return True
    session.close()
    return False

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

# create_product("Стильная футболка Nike", "Оригинальная футболка из натуральной и мягкой ткани", 5300)
print(get_products())

