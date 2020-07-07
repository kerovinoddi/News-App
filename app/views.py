from flask import render_trmplate
from app import app

#Views
@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    View root page function that returns the news page and its data
    '''

    return render_template('news.html',id = news_id)

from .request import get_news


@app.route('/')
def index():

