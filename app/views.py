from flask import render_trmplate,request,redirect
from app import app
from ..request import get_sources,get_articles
from ..models import Sources

#Views
@app.route('/')
def index():
    '''
    View root page function that returns the news page and its data
    '''
    source = get_sources('business')
    sports_sources = get_sources('sports')
    entertainment_sources = get_sources('entertainment')
    technology_sources = get_sources('technology')
    title = "News Highlight"

    return render_template('news.html',title = title,sources = sources,sports_sources = sports_sources,technology_sources = technology_sources,entertainment_sources = entertainment_sources)

@app.route('/sources/<id>')
def articles(id):


    '''
    View method that returns articles
    '''

    #Getting views 
    articles = get_articles(id)
    print(news)#####
    title = 'Welcome to news review website'
    return render_template('index.html',title = title,new=news_highlights)





