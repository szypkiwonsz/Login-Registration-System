from flask import flash, redirect, url_for
from database import Database
import re


class User(Database):

    # Check if user exist.
    @staticmethod
    def user_exist(login, email):

        database = User('users_data.sqlite')
        login = database.select_login(login)
        # Checking if typed email is already used by user.
        email = database.select_email(email)
        if login or email:
            pass
        else:
            database.close()
            flash('User not exist!')
            return redirect(url_for('/'))

    # Checks if already user with this login or email exist.
    @staticmethod
    def exist(login, email):

        database = User('users_data.sqlite')
        # Checking if typed login is already used by user.
        login = database.select_login(login)
        # Checking if typed email is already used by user.
        email = database.select_email(email)

        if login or email:
            database.close()
            flash('User already exist!')
            return redirect(url_for('/'))
        else:
            pass

    # Checks if email is typed in good form.
    @staticmethod
    def email(email):
        return re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)

    # Checks if login or password has good length of characters.
    @staticmethod
    def characters(login, password):
        if 6 > len(str(login)) > 0 or 6 > len(str(password)) > 0:
            flash('Login or password too short!')
            return redirect(url_for('/'))
        else:
            pass

    # Check if login, email or password has been filled without spaces.
    @staticmethod
    def spaces(login, email, password):
        if " " in login or " " in email or " " in password:
            flash("You can't use spaces!")
            return redirect(url_for('/'))
        else:
            pass
