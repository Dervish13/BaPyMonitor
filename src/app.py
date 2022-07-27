import os

from flask import Flask

import src.globals_init as globals_init
from src.api import blueprints
from src.config.config import configs
from src.register import register_endpoints


def create_app():
    config_name = os.getenv('CONFIG_NAME')

    config = configs[config_name]

    globals_init.initialize_globals()

    app = Flask(__name__)
    app.config.from_object(config)

    register_endpoints(app, blueprints)

    return app


application = create_app()
