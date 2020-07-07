from app import app
import urllib.request,json
from models import news


News = news.News
#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the movie base url
base_url = app.config["MOVIE_API_BASE_URL"]

def get_news(category):
    '''
    Functipon that gets json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    
    with urllib.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        movies_results = None

        if get_news_response['result']:
            news_result_list = get_movies_response['result']
            news_result = process_result(movie_results_list)

    return movie_results