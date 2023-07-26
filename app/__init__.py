"""Initialize app."""
from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    """Construct the core app object."""
    app = Flask(__name__, instance_relative_config=False)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SECRET_KEY'] = 'sfdsfsdgsdgs'

    # Initialize Plugins
    db.init_app(app)

    with app.app_context():

        # Register Blueprints
        from app.home.home_blueprints import home_blueprints
        app.register_blueprint(home_blueprints)

        from app.purchase.purchase_blueprints import purchase_blueprints
        app.register_blueprint(purchase_blueprints)

        from app.status.status_blueprints import status_blueprints
        app.register_blueprint(status_blueprints)

        # Create Database Models
        db.create_all()
        db.session.commit()

        # Compile static assets
        # if app.config["FLASK_ENV"] == "development":
        #     compile_static_assets(app)

        return app
