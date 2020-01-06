from flask import Flask, render_template, request, json, flash, url_for, redirect
from database import Database
from user import User
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'szypkiwonsz'

user = User('users_data.sqlite')

# Creates main page.
@app.route('/')
def main():

    return render_template('index.html')


@app.route('/signUp', methods=['POST'])
def sign_up():

    try:
        # Getting user data.
        login = request.form['inputName']
        email = request.form['inputEmail']
        password = request.form['inputPassword']

        user.characters(login, password)
        user.spaces(login, email, password)

        # Hashing password.
        password = generate_password_hash(password)

        # Checking if mail is typed in good form.
        email_match = user.email(email)

        # Checking if all data is typed and the form is in good form.
        if login and email and password and email_match:
            database = Database('users_data.sqlite')
            # Creating table USERS if that not exist.
            database.create('USERS')

            user.exist(login, email)

            database.insert(login, email, password)
            database.close()
            flash('User correctly registered.')
            return redirect(url_for('/'))

        else:
            flash('Fields filled incorrectly!')
            return redirect(url_for('/'))

    except Exception as e:
        return json.dumps({'error': str(e)})


@app.route('/signIn', methods=['POST'])
def sign_in():

    try:
        # Getting data typed by user.
        login = request.form['putName']
        email = request.form['putEmail']
        password = request.form['putPassword']

        # Checking if all data is typed.
        if login and email and password:

            database = Database('users_data.sqlite')
            user.user_exist(login, email)
            data = database.select_password(login, email)
            database.close()
            # Checking if password is typed correctly.
            if check_password_hash(data[0][0], password):
                flash('Correctly logged in.')
                return redirect(url_for('/'))
            else:
                flash('Wrong Password!')
                return redirect(url_for('/'))
        else:
            flash('Fields are unfilled!')
            return redirect(url_for('/'))

    except Exception as e:
        return json.dumps({'error': str(e)})


if __name__ == '__main__':
    app.run(port=5002)
