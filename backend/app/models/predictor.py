import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

class WeightPredictor:
    def __init__(self):
        self.model = None
        self.min_date = None

    def init_app(self, app):
        """Initialize with data from data_loader"""
        from app.models.data_loader import data_loader  # Import here to avoid circular imports
        df = data_loader.get_data()
        self.train_model(df)

    def train_model(self, df):
        """Train the linear regression model"""
        if 'Date' not in df.columns or 'Weight' not in df.columns:
            raise ValueError("Dataset must contain 'Date' and 'Weight' columns")

        self.min_date = df['Date'].min()
        df['Days'] = (df['Date'] - self.min_date).dt.days
        df['Weight'] = df['Weight'].interpolate()

        X = df['Days'].values.reshape(-1, 1)
        y = df['Weight'].values

        if len(X) == 0 or len(y) == 0:
            raise ValueError("No valid data available for training")

        self.model = LinearRegression()
        self.model.fit(X, y)

    def predict(self, days_ahead: int):
        """Predict future weights"""
        future_dates = [datetime.now() + timedelta(days=i) for i in range(days_ahead + 1)]
        future_days = np.array([(date - self.min_date).days for date in future_dates]).reshape(-1, 1)
        return self.model.predict(future_days), future_dates

# Create instance here
predictor = WeightPredictor()