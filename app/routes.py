from flask import Blueprint, render_template, redirect, url_for
from flask import render_template, url_for, flash, redirect, Blueprint
from app import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from app.models import User
from app.forms import UpdateAccountForm

bp = Blueprint('routes', __name__)

@bp.route("/")
@bp.route("/home")
def home():
    return render_template('home.html')

@bp.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('routes.profile'))
    return render_template('profile.html', form=form)
