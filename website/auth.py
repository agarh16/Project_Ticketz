from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
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

        
        if len(firstName) < 2:
            #Flash a message
            flash('First name must be greater than 1 character.', category='error')
        elif len(lastName) < 2:
            #Flash a message
            flash('Last name must be greater than 1 character.', category='error')
        elif len(email) < 4:
            #Flash a message
            flash('Email must be greater than 4 characters.', category='error')
        elif len(password1) < 7:
            #Flash a message
            flash('Password must have at least 7 characters.', category='error')
        elif password1 != password2:
            #Flash a message
            flash('Passwords do not match.', category='error')
        else: 
            return "HELLO"    
                
    return render_template("sign_up.html")



