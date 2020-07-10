from flask import render_template
from . import models

@model.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function ro render 404 error page
    '''

    return render_template('404.html'),404
