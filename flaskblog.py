from flask import Flask, render_template,url_for
from forms import RegistrationForm,LogininForm
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
@app.route('/Register')
def Register():
    form = RegistrationForm()
    return render_template('register.htm', form=form)
@app.route('Loginr')
def Logi():
    form = RegistrationForm()
    return render_template('Login.htm', form=form)
      


if __name__ == "__main__":
    app.run(debug=True)
