
from flask import Flask

import os
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
# __name__ is a built in variable that refers to the local python file we're working with

# DB Connection

# suppress SQLAlchemy warning
app.config['SQALCHEMY_TRACK_MODIFICATIONS'] = False
# get abs path to the app dir to create the db here
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'blog.db')
app.config['SECRET_KEY'] = '50a3b7cc91918d658cddc43d7ad46af1411a0bad2daf66c0'
db = SQLAlchemy(app)

# to create db, import:

# >>> from blog import app, db
# >>> with app.app_context():
# ...     db.create_all()


# this <from blog import routes> should be HERE BELOW in the last line (or after app.config) as the order of imports in the _init_.py file is important. The last thing this script should do is import the routes.py file.

from blog import routes

# end of exlaination
