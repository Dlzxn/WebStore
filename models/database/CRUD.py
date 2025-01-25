from models.database.create_table import User, SessionLocal

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

get_users("admin", "<PASSWORD>")
