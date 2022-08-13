from flask import render_template, redirect, url_for, flash,get_flashed_messages
from market import app, db
from market.models import Item, User
from market.forms import RegisterForm


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data, password_hash=form.password1.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(err,category='danger')
    return render_template('register.html', form=form)