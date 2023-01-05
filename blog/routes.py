from flask import render_template, url_for, request, redirect
# url_for is to to avoid handling of URLs manually (e.g. if we change a root URL we would need to change all templates/web page this URL is present).
# Look at layout page for usage
from blog import app, db
from blog.models import User, Post
from blog.forms import RegistrationForm


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


@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('registered'))
    return render_template('register.html',title='Register',form=form)