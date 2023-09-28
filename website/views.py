# Store all the main views or the URL endpoints 
from flask import Blueprint, render_template, request, session
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    # if user is client 
    return render_template("home_client.html")

    #if user is employee
    #return render_template("home_employee.html")




    
