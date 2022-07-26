import os

from flask import Flask

from src.api import blueprints
from src.config.config import configs
from src.register import register_endpoints

config_name = os.getenv('CONFIG_NAME')

config = configs[config_name]

application = Flask(__name__)
application.config.from_object(config)


register_endpoints(application, blueprints)

if __name__ == '__main__':
    application.run()
