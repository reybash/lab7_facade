import lab7_facade as facade


# Использование фасада
def main():
    db_facade = facade.DatabaseFacade("sqlite:///example.db")
    print_facade = facade.PrintUsersDatabaseFacade()

    db_facade.add_user("Alice", 25)
    db_facade.add_user("Bob", 30)

    print_facade.print_users(db_facade)

    db_facade.update_user_age(1, 26)

    print_facade.print_users(db_facade)


if __name__ == "__main__":
    main()
