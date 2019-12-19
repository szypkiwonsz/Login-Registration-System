from flask import flash, redirect, url_for
from database import Database
import re


class User:

    # Checks if already user with this login or email exist.
    @staticmethod
    def exist(login, email):

        database = Database('users_data.sqlite')
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
        if len(str(login)) < 6 or len(str(password)) < 6:
            flash('Login or password too short!')
            return redirect(url_for('/'))
        else:
            pass
