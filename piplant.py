from flask import (
  Flask, render_template, request, flash, redirect, url_for, session
)
#from models import db
import db
from werkzeug.security import generate_password_hash, check_password_hash

votr = Flask(__name__)
#todo - secure the secret key.
votr.secret_key = 'myKey'

# load config from the config file we created earlier
#votr.config.from_object('config')

@votr.route('/')
def home():
    return render_template('index.html')

@votr.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # hash the password
        password = generate_password_hash(password)

        error = db.votr_UserSignup(email, username, password)
        if error > 0:
            flash("Email is already in use. ")
        else:
            return redirect(url_for('home'))

    return render_template('signup.html')

@votr.route('/polls')
def polls():
    return render_template('polls.html')

@votr.route('/login', methods=['POST'])
def login():
    # we don't need to check the request type as flask will raise a bad request
    # error if a request aside from POST is made to this url

    email = request.form['username']
    password = request.form['password']

    username, password_hash = db.votr_Userlookup(email)
    '''
    if password_hash:

        if check_password_hash(password_hash, password):
            # The hash matches the password in the database log the user in
            session['user'] = username
            flash('Login was succesfull')
    else:
        # user wasn't found in the database
        flash('Username or password is incorrect please try again', 'error')
    '''

    return redirect(url_for('home'))

@votr.route('/')
def schedule():
    pass
    #return render_template('index.html')

if __name__ == '__main__':
    votr.run(host='0.0.0.0')
