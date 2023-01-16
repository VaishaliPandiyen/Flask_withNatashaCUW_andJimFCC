from blog import app

# checks if wsgi.py is executed directly (not imported):
if __name__ == '__main__':
    app.run(debug=True)
