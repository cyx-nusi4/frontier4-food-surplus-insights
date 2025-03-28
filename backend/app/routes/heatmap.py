from flask import Blueprint, jsonify, request
from datetime import datetime
from app.extensions import data_loader
import pandas as pd

heatmap_bp = Blueprint('heatmap', __name__)

# Area location mapping
AREA_LOCATIONS = {
    "Bukit Batok": (1.3496, 103.7493), "Geylang": (1.3180, 103.8930),
    "Bishan": (1.3508, 103.8485), "Hougang": (1.3714, 103.8925),
    "Bukit Timah": (1.3294, 103.8021), "Tampines": (1.3540, 103.9439),
    "Punggol": (1.4039, 103.9103), "Serangoon": (1.3500, 103.8733),
    "Choa Chu Kang": (1.3850, 103.7444), "Woodlands": (1.4380, 103.7880),
    "Kallang": (1.3121, 103.8650), "Bedok": (1.3236, 103.9307),
    "Sengkang": (1.3917, 103.8950), "Novena": (1.3201, 103.8442),
    "Toa Payoh": (1.3341, 103.8504), "Clementi": (1.3151, 103.7641),
    "Tanglin": (1.3085, 103.8074), "Marine Parade": (1.3039, 103.9051),
    "Outram": (1.2806, 103.8390), "Jurong East": (1.3334, 103.7420),
    "Bukit Panjang": (1.3786, 103.7612), "Bukit Merah": (1.2770, 103.8190),
    "Queenstown": (1.2945, 103.7856), "Ang Mo Kio": (1.3691, 103.8454),
    "Jurong West": (1.3446, 103.7053), "Pasir Ris": (1.3730, 103.9497),
    "Yishun": (1.4294, 103.8354), "Tengah": (1.3667, 103.7222),
    "Sembawang": (1.4450, 103.8185), "Downtown Core": (1.2820, 103.8510),
    "Western Water Catchment": (1.4053, 103.6900), "Changi": (1.3644, 103.9915)
}


@heatmap_bp.route('/heatmap', methods=['GET'])
def generate_heatmap():
    start_date_str = request.args.get('startDate', '2024-01-01')
    end_date_str = request.args.get('endDate', '2024-12-31')

    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    df = data_loader.get_data()

    # Data processing
    df_filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    if df_filtered.empty:
        return jsonify({"error": "No data available for the selected date range"}), 400

    df_filtered['Latitude'] = df_filtered['Area'].map(lambda x: AREA_LOCATIONS.get(x, (None, None))[0])
    df_filtered['Longitude'] = df_filtered['Area'].map(lambda x: AREA_LOCATIONS.get(x, (None, None))[1])

    df_cleaned = df_filtered.dropna(subset=['Latitude', 'Longitude', 'Weight'])
    heat_data = [[row['Latitude'], row['Longitude'], row['Weight']] for _, row in df_cleaned.iterrows()]

    return jsonify({"heat_data": heat_data})