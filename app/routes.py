from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.forms import RegistrationForm, LoginForm, UpdateProfileForm
from app.models import User
from app import create_app

app = create_app()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password.')
    return render_template('login.html', form=form)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        if form.password.data:
            current_user.set_password(form.password.data)
        db.session.commit()
        flash('Profile updated successfully!')
        return redirect(url_for('profile'))
    form.username.data = current_user.username
    form.email.data = current_user.email
    return render_template('profile.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


