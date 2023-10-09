from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# Определение модели данных
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


# Фасад для работы с базой данных
class DatabaseFacade:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_user(self, name, age):
        new_user = User(name=name, age=age)
        self.session.add(new_user)
        self.session.commit()

    def get_users(self):
        return self.session.query(User).all()

    def update_user_age(self, user_id, new_age):
        user = self.session.query(User).filter(User.id == user_id).one()
        user.age = new_age
        self.session.commit()

    def __del__(self):
        self.session.close()


class PrintUsersDatabaseFacade:
    def __init__(self):
        pass

    def print_users(self, db_facade):
        users = db_facade.get_users()
        for user in users:
            print(f"User ID: {user.id}, Name: {user.name}, Age: {user.age}")
