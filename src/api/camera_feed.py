from flask import Blueprint
from flask.wrappers import Response

import src.globals_init as globals_init
from src.helpers.camera.camera_helper import gen

blueprint = Blueprint('camera', 'camera')

@blueprint.route('/easter_egg')
def tandara():
    return("mandara")


@blueprint.route('/')
def video_feed():
    return Response(gen(globals_init.video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
