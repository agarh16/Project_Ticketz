# Store all the main views or the URL endpoints 
from flask import Blueprint, render_template, request, session

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # if user is client 
    return render_template("home_client.html")

    #if user is employee
    #return render_template("home_employee.html")




    
