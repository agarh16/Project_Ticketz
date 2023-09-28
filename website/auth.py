from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Query to check if user already exists.
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password. Try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("logout.html")

@auth.route('sign-up', methods=['GET', 'POST'])
def sing_up():

    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        isEmployee = request.form.get('isEmployee')

        # Query to check if user already exists.
        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(firstName) < 2:
            # Flash a message
            flash('First name must be greater than 1 character.', category='error')
        elif len(lastName) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif password1 != password2:
            flash('Passwords do not match.', category='error')
        elif len(password1) < 7:
            flash('Password must have at least 7 characters.', category='error')
        elif isEmployee == '1': 
            new_user = User(firstName=firstName, lastName=lastName, email=email, password=generate_password_hash(password1, method='sha256'), isEmployee=True)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for("views.home"))    
        else:
            new_user = User(firstName=firstName, lastName=lastName, email=email, password=generate_password_hash(password1, method='sha256'), isEmployee=False)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            
            return redirect(url_for('views.home'))           
    
    return render_template("sign_up.html")



