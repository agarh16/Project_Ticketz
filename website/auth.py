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
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        isEmployee = request.form.get('isEmployee')

        if len(email) < 4:
            #Flash a message
            pass
        elif len(firstName) < 2:
            #Flash a message
            pass
        elif len(lastName) < 2:
            #Flash a message
            pass
        elif len(password1) < 7:
            #Flash a message
            pass
        elif password1 != password2:
            #Flash a message
            pass
        else: 
            # add user to database
            pass
    return render_template("sign_up.html")



