import os
import pandas as pd
from functools import lru_cache


class CSVDataLoader:
    def __init__(self):
        self.csv_path = None

    def init_app(self, app):
        self.csv_path = os.path.abspath(app.config.get('DATA_FILE_PATH'))
        if not os.path.exists(self.csv_path):
            raise FileNotFoundError(f"CSV file not found at {self.csv_path}")

    @lru_cache(maxsize=1)
    def load_data(self) -> pd.DataFrame:
        """Load and cache CSV data with proper formatting"""
        df = pd.read_csv(self.csv_path, encoding="latin1")

        # Data cleaning and transformation
        df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d', errors='coerce')
        # print(df['Date'])
        df['Year-Month'] = df['Date'].dt.to_period("M")
        df["Weight"] = pd.to_numeric(
            df["Weight"].astype(str).str.replace("KG", "", case=False),
            errors="coerce"
        ).fillna(0)

        return df

    def get_data(self) -> pd.DataFrame:
        """Public method to get the cached data"""
        return self.load_data()


# Create instance here
data_loader = CSVDataLoader()