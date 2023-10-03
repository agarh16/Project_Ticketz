# Store all the main views or the URL endpoints 
from flask import Blueprint, render_template, request, session
from flask_login import login_required, current_user
from . import db
from .models import User

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    
    return render_template("home.html", user=current_user)

    

@views.route('/test-database')
def all_users_table():
    results = db.session.query(User).all()
    for result in results:
        printed_results = result.firstName, result.lastName, result.email, result.isEmployee
        print(printed_results)
    return render_template("test.html")




    
