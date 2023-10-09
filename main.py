import lab7_facade as facade


# Использование фасада
def main():
    db_facade = facade.DatabaseFacade("sqlite:///example.db")

    db_facade.add_user("Alice", 25)

    db_facade.add_user("Bob", 30)

    db_facade.update_user_age(1, 26)


if __name__ == "__main__":
    main()
