import pytest
from lab7_facade import DatabaseFacade


@pytest.fixture
def db_facade():
    db_url = "sqlite:///:memory:"
    return DatabaseFacade(db_url)


def test_add_user(db_facade):
    db_facade.add_user("Alice", 25)
    user = db_facade.get_users()[0]
    assert user.name == "Alice"
    assert user.age == 25


def test_update_user_age(db_facade):
    db_facade.add_user("Alice", 25)
    db_facade.update_user_age(1, 26)
    user = db_facade.get_users()[0]
    assert user.age == 26


def test_get_users_empty(db_facade):
    assert db_facade.get_users() == []


def test_get_users_multiple_users(db_facade):
    db_facade.add_user("Alice", 25)
    db_facade.add_user("Bob", 30)
    users = db_facade.get_users()
    assert len(users) == 2
    assert users[0].name == "Alice"
    assert users[1].name == "Bob"


# Падающий тест: попытка обновить возраст несуществующего пользователя
def test_update_nonexistent_user_age(db_facade):
    with pytest.raises(Exception):
        db_facade.update_user_age(1, 26)


# Падающий тест: попытка получить список пользователей перед добавлением
def test_get_users_before_adding(db_facade):
    assert db_facade.get_users() != []


# Падающий тест: попытка добавить пользователя с отрицательным возрастом
def test_add_user_with_negative_age(db_facade):
    with pytest.raises(Exception):
        db_facade.add_user("Alice", -25)
