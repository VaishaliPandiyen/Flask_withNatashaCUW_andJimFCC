
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '50a3b7cc91918d658cddc43d7ad46af1411a0bad2daf66c0'

# this <from blog import routes> should be here in the last line (or after app.config) as the order of imports in the _init_.py file is important. The last thing this script should do is import the routes.py file.
from blog import routes
# end of exlaination