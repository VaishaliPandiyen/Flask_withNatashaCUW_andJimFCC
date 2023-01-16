from flask import render_template, url_for, request, redirect, flash
# url_for is to to avoid handling of URLs manually (e.g. if we change a root URL we would need to change all templates/web page this URL is present).
# Look at layout page for usage
from blog import app, db
from blog.models import User, Post
from blog.forms import RegistrationForm
from blog.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, current_user


@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', title='Home', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About Me')


@app.route("/about/<username>")
def about_withName(username):
    items = [
        {1: 'alpha', 2: 'beta'},
        {1: 'one', 2: 'two'},
        {1: 'first', 2: 'second'}
    ]
    return render_template('about.html', title=f'About {username}', name=f'{username}', items=items)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    hashed_password=form.password.data,email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!')
        return redirect(url_for('registered'))
    return render_template('register.html', title='Register', form=form)


@app.route("/registered")
def registered():
    form = RegistrationForm()
    return render_template('registered.html', title='Thanks!', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('You\'ve successfully logged in,'+' '+ current_user.username +'!')
            return redirect(url_for('home'))
        flash('Invalid username or password.')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash('Logout successful. Bye!')
    return redirect(url_for('home'))
