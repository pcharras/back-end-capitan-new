

from .project_api import project_api_blueprint
from .stage_api import stage_api_blueprint
from .project_stage_api import project_stage_api_blueprint
from .thread_api import thread_api_blueprint
from .message_api import message_api_blueprint
# Puedes definir otros Blueprints para diferentes partes de tu API y registrarlos aquí

def init_api(app):
    app.register_blueprint(project_api_blueprint, url_prefix='/api')
    app.register_blueprint(stage_api_blueprint, url_prefix='/api')
    app.register_blueprint(project_stage_api_blueprint, url_prefix='/api')
    app.register_blueprint(thread_api_blueprint,url_prefix='/api')
    app.register_blueprint(message_api_blueprint,url_prefix='/api')