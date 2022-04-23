from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user, login_manager

auth = Blueprint('auth', __name__)

# Mensaje mostrado cuando un usuario no logeado intenta acceder
login_manager.LOGIN_MESSAGE = "Debes estar logeado para acceder a la pagina"

@auth.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        #new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        #db.session.add(new_user)
        #db.session.commit()
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Te has logeado satisfactoriamente!!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.stock'))
            else:
                flash('Contraseña Incorrecta', category='error')
        else:
            flash('El usuario ingresado no existe', category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))