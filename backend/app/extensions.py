from .models.data_loader import data_loader
from .models.predictor import predictor

# No need to recreate instances here, just import the existing ones

def init_data_loader(app):
    data_loader.init_app(app)

def init_predictor(app):
    predictor.init_app(app)