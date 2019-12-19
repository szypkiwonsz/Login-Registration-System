### Simple login and registration system build in Python, using flask framework and SQLite database system. 

##### The program do:
- Inserts correctly registered user into database.
- Passwords are hashing before inserting into database.
- Checks if user correctly logged in. 

##### The program checks: 
- If the user has entered login and password longer than 5 characters.
- If the user has entered email in good form (has “@” and “.” sign)
- If the user has entered data that is not already in database.
- If the user has filled all fields.

##### Packages to install:
- pip install -U Flask
- pip install -U Werkzeug

##### Version of software used:
- Python 3.7.x
- Flask 1.1.1
