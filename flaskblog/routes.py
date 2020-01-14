from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm


posts = [
    {
        'author': ' Simon Kimani',
        'title': 'Blog post 1',
        'content': 'First post Content',
        'date_posted': 'January 9, 2020'
    },
    {
        'author': ' Anthony Professor',
        'title': 'Blog post 2 ',
        'content': 'First post Content',
        'date_posted': 'January 9, 2020'
    }
]
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.htm', posts=posts)


@app.route('/about')
def about():
    return render_template('about.htm')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.date, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        
        flash(
            f'You have successfully created an account for {form.username.data}! You can now log in to your account','success')
        return redirect(url_for('home'))
    return render_template('register.htm', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.htm', form=form)