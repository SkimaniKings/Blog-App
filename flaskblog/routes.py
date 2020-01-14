from models import User, Post

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