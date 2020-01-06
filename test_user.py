import pytest
from user import User


def test_exist():
    database = User("users_data.sqlite")


def test_email():
    match_email = User.email("test_email")
    assert match_email is None
    match_email = User.email("test_email@gmail.com")
    assert match_email is not None

