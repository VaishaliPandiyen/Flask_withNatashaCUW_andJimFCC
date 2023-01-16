1. to create db, tpe this in python cli:

from blog import app, db
with app.app_context():
...  db.create_all()

_________________________


2. you can create a user/post from cli like this:

# 2.1. Natasha's way:
    -- sqlite CLI

INSERT INTO user (username,email) VALUES ('johnsmith','john@smith.com');

[for bulk adding, ref. to pdf 2 ste 10]

# 2.2. Jim's way:
    -- python CLI

userX = User(username="mahagony", password="xdcfgvhbjnkml", email="papaya@crow.com")

db.session.add(userX)
db.session.commit()

+ To see the added items:

User.query.all()
- similar to what we write in route.py

for user in User.query.filter_by(email="papaya@crow.com"):
    user.username


_________________________


3. delete database before creating a fresh one (in case of changes)

# Jim's way:
    -- python cli

from blog import db
db.drop_all()
with app.app_context():
...  db.create_all()

db.session.rollback()
- to rollback this python session's commits and changes
