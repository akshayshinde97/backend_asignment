"""
Api application file
"""

# local imports
from .routes import api_bp
# from datadaemon import init_daemon

def init_app(app):
    """
    initialize Api app
    """
    app.register_blueprint(api_bp, url_prefix='/api')
    # init_daemon()
