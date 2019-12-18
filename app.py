from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)

# Creates main page.
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/signUp', methods=['GET'])
def sign_up():

    try:
        login = request.form['inputName']
        email = request.form['inputEmail']
        password = request.form['inputPassword']

        if:



if __name__ == '__main__':
    database = Database('users_data.sqlite')
    database.create('USERS')
    app.run()
