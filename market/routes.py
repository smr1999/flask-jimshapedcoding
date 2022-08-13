from crypt import methods
from flask import render_template, redirect, url_for, flash
from market import app, db
from market.models import Item, User
from market.forms import RegisterForm,LoginForm
from flask_login import login_user

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
                    email=form.email.data, password=form.password1.data)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully .",category="success")
        return redirect(url_for('login_page'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(err,category='danger')
    return render_template('register.html', form=form)

@app.route('/login',methods=["GET","POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash(f"Success ! You are logged in as {user.username} .",category="success")
            return redirect(url_for("market_page"))
        else:
            flash("Username Or Password is not matched ! Please try again .",category="danger")
    return render_template("login.html",form=form)
