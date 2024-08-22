from flask import Blueprint, render_template
from app import db, bcrypt
from flask_login import login_required

bp = Blueprint('main', __name__)

@bp.route('/')
@login_required
def home():
    return render_template('home.html')



# Другие маршруты для регистрации, входа и выхода пользователя
# from flask import render_template, url_for, flash, redirect, request
# from app import app, db, bcrypt
# from app.forms import RegistrationForm, LoginForm, EditProfileForm
# from app.models import User
# from flask_login import login_user, current_user, logout_user, login_required
#
# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template('home.html')
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(user)
#         db.session.commit()
#         flash('Ваш аккаунт был создан! Теперь вы можете войти.', 'success')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Регистрация', form=form)
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password, form.password.data):
#             login_user(user, remember=form.remember.data)
#             return redirect(url_for('home'))
#         else:
#             flash('Вход не выполнен. Проверьте email и пароль.', 'danger')
#     return render_template('login.html', title='Вход', form=form)
#
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('home'))
#
# @app.route('/edit_profile', methods=['GET', 'POST'])
# @login_required
# def edit_profile():
#     form = EditProfileForm()
#     if form.validate_on_submit():
#         current_user.username = form.name.data
#         current_user.email = form.email.data
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         current_user.password = hashed_password
#         db.session.commit()
#         flash('Ваш профиль был успешно обновлен!', 'success')
#         return redirect(url_for('home'))
#     elif request.method == 'GET':
#         form.name.data = current_user.username
#         form.email.data = current_user.email
#     return render_template('edit_profile.html', title='Редактировать профиль', form=form)
