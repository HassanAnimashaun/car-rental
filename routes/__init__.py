from flask import Flask

def create_app():
    # Initialize Flask app and specify the path to the templates folder
    app = Flask(__name__, template_folder='../templates')

    # Configuration settings
    app.config['SECRET_KEY'] = 'SUPERSECRETKEY'  # Change this to a secure random key

    # Import and register Blueprints
    from .main_routes import main_routes
    from .auth_routes import auth_routes
    from .invoice_processing import invoice_processing

    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(invoice_processing)

    return app
