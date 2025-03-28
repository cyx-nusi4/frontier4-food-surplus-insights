from flask import Blueprint, jsonify
from app.extensions import data_loader

statistics_bp = Blueprint('statistics', __name__)

@statistics_bp.route('/requests', methods=['GET'])
def get_requests_by_area():
    df = data_loader.get_data()
    area_requests = df.groupby("Area")["Requests"].sum()
    requests_points = [{"x": area, "y": value} for area, value in
                      sorted(area_requests.items(), key=lambda item: item[1], reverse=True)]
    return jsonify({"points": requests_points})

@statistics_bp.route('/weights', methods=['GET'])
def get_weights_by_area():
    df = data_loader.get_data()
    area_weight = df.groupby("Area")["Weight"].sum()
    weight_points = [{"x": area, "y": value} for area, value in
                    sorted(area_weight.items(), key=lambda item: item[1], reverse=True)]
    return jsonify({"points": weight_points})