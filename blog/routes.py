from flask import render_template, url_for
# url_for is to to avoid handling of URLs manually (e.g. if we change a root URL we would need to change all templates/web page this URL is present).
# Look at layout page for usage
from blog import app
from blog.models import User, Post


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')


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
