from flask import Blueprint
main = Blueprint('models',__name__)
from . import views,errors
