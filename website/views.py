# Store all the main views or the URL endpoints 
from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/')
def home():
   
    return render_template("home_client.html")


    
