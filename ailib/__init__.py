from flask import Flask
from ailib.blueprints.ai_lib_api import api_bp
from ailib.blueprints.ai_lib_web import web_bp
from ailib.connectors.openai import ailib_openai

from flask import Flask

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    
    # load the configuration using the name
    if config_name == 'dev':
        from ailib.instance.config import Dev
        app.config.from_object(Dev)
    elif config_name == 'prod':
        from ailib.instance.config import Prod
        app.config.from_object(Prod)
    elif config_name == 'test':
        from ailib.instance.config import Test
        app.config.from_object(Test)

    # init extentions
    app.openai = ailib_openai(app)

    # register blueprints
    app.register_blueprint(api_bp)
    if not app.config['DISABLE_UI']:
        app.register_blueprint(web_bp)
        
    return app

