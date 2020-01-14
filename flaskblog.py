from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = '6f537a0de4d614ba210441a2049f30d0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True,  nullable=False)
    image_file = db.Column(db.String(20), unique=True,nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref ='author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'),nullable = False)
    
def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


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
        flash(
            f'You have successfully created an account for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.htm', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.htm', form=form)


if __name__ == "__main__":
    app.run(debug=True)
