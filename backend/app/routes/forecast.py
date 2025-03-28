from flask import Blueprint, jsonify, request
from datetime import datetime
from app.extensions import predictor

forecast_bp = Blueprint('forecast', __name__, url_prefix='/forecast')


@forecast_bp.route('/byWeight', methods=['GET'])
def predict_future_weight():
    days_ahead = request.args.get('duration', default=10, type=int)

    try:
        future_weights, future_dates = predictor.predict(days_ahead)
        show_points = days_ahead <= 60

        predictions = [
            {"x": date.strftime('%Y-%m-%d'), "y": weight, "show_point": show_points}
            for date, weight in zip(future_dates, future_weights)
        ]

        return jsonify({"points": predictions, "show_points": show_points})
    except Exception as e:
        return jsonify({"error": str(e)}), 500