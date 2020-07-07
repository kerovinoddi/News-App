
class Config:    
    '''
    General configuration parent class
    '''
     NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


    pass

class ProdConfig(Config):
    '''
    Producyion configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration setting
    '''

    DEBUG = True

