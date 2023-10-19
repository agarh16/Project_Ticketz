# Store all the main views or the URL endpoints 
from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import User, Ticket

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    
    return render_template("home.html", user=current_user)

    

@views.route('/test-database')
def all_users_table():
    results = db.session.query(User).all()
    # for result in results:
    #     printed_results = result.firstName, result.lastName, result.email, result.isEmployee
    #     print(printed_results)
    return render_template("test.html", user=current_user, results=results)

@views.route('/create-ticket', methods=['GET','POST'])
@login_required
def create_ticket():
    if request.method == 'POST':
        ticketName = request.form.get('ticketName')
        ticketText = request.form.get('ticketText')
        

        if len(ticketName) < 2:
            flash('Ticket name must be greater than 1 character.', category='error')
            return redirect(url_for('views.create_ticket')) 
        elif len(ticketText) < 2:
            flash('Text must be grater than 1 chatacter.', category='error')
            return redirect(url_for('views.create_ticket')) 
        else:
            new_ticket = Ticket(ticketName=ticketName, userId=current_user.id, ticketText=ticketText)
            db.session.add(new_ticket)
            db.session.commit()
            flash('Ticket created!', category='success')
        
        return render_template("home.html", user=current_user)           

    return render_template("create_ticket.html", user=current_user)

    
