from flask import Flask, render_template,url_for,flash
from forms import RegistrationForm,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '6f537a0de4d614ba210441a2049f30d0'

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
@app.route('/register', methods= ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'You have successfully created an account for {form.username.data}!')
    return render_template('register.htm', form=form)
@app.route('/login')
def login():
    form =LoginForm()
    return render_template('login.htm', form=form)
      


if __name__ == "__main__":
    app.run(debug=True)
