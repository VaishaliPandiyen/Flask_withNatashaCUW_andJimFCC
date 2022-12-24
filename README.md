TO RUN THE FLASK APP:

create the virtual environment:
> py -m venv venv

activate it:
> venv\Scripts\activate 

and then install flask:
> pip install flask

Enable the debug mode:
> set FLASK_DEBUG=True

Tell Flask where to find your app:
> set FLASK_APP=wsgi

Start the development server:
> flask run

* * * * *

In case of difficulty in running python or flask due to change in path(s) - both relative and absolute:

1. Delete venv and pycache folder
2. Follow all CLI instructions, starting from create the virtual environment (pg.3) to start the development server (pg.4) on the FLASK_1_EXERCISES.pdf
