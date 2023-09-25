# Store all the main views or the URL endpoints 
from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"

