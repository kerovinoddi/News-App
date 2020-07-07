from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_config = True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.form_pyfile('config.py')


from app import views

