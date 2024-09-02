from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuration settings
    app.config['SECRET_KEY'] = 'SUPERSECRETKEY'  # Change this to a secure random key

    # Import routes and authentication routes
    from . import main_routes
    from .auth_routes import auth_bp

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_routes.main_bp)  # Register main routes blueprint

    return app
