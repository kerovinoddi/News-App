from views import render_trmplate
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')