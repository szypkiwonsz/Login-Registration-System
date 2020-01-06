import pytest
from database import Database


@pytest.fixture(scope="module")
def database():
    database = Database("users_data.sqlite")
    database.create("USERS")
    database.insert("filled_test_login", "filled_test_email@gmail.com", "filled_test_password")

    database.test_user = [(1, "filled_test_login", "filled_test_email@gmail.com", "filled_test_password")]
    yield database

    database.cursor.execute("DROP TABLE USERS")
    database.close()


def test_select_email(database):
    query = database.select_email("empty_test_email@gmail.com")
    assert query == []
    query = database.select_email("filled_test_email@gmail.com")
    assert query == database.test_user


def test_select_login(database):
    query = database.select_login("empty_test_login")
    assert query == []
    query = database.select_login("filled_test_login")
    assert query == database.test_user


def test_select_password(database):
    query = database.select_password("empty_test_login", "empty_test_email")
    assert query == []
    query = database.select_password("filled_test_login", "filled_test_email@gmail.com")
    assert query[0][0] == database.test_user[0][3]


def test_insert(database):
    database.insert("insert_test_login", "insert_test_mail@gmail.com", "insert_test_password")
    query = database.select_login("insert_test_login")
    assert query == [(2, "insert_test_login", "insert_test_mail@gmail.com", "insert_test_password")]
