from flask import Blueprint

blueprint = Blueprint('camera', __name__)

@blueprint.route('/')
def tandara():
    return("mandara")
