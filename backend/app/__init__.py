from flask import Flask
from .extensions import data_loader, predictor
from .routes.forecast import forecast_bp
from .routes.heatmap import heatmap_bp
from .routes.statistics import statistics_bp


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Initialize extensions with app context
    data_loader.init_app(app)
    predictor.init_app(app)

    # Register blueprints
    app.register_blueprint(forecast_bp)
    app.register_blueprint(heatmap_bp)
    app.register_blueprint(statistics_bp)

    return app