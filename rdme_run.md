TO RUN THE FLASK APP:

create the virtual environment:
> py -m venv venv

activate it:
> venv\Scripts\activate 

and then install flask:
> pip install flask

Enable the debug mode:
> set FLASK_DEBUG=True
1. This is to allow your app to sync whenever you change the code
2. This is only for dev mode, not for production or deployment as it will show bugs for the app users

Tell Flask where to find your app:
> set FLASK_APP=wsgi

Start the development server:
> flask run
