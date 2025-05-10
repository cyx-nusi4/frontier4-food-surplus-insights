from flask import Blueprint, jsonify
from app.extensions import data_loader

statistics_bp = Blueprint('statistics', __name__)

# TODO add date range search
@statistics_bp.route('/food/requests', methods=['GET'])
def get_requests_by_area():
    df = data_loader.get_data()
    area_requests = df.groupby("Area")["Requests"].sum()
    requests_points = [{"x": area, "y": value} for area, value in
                      sorted(area_requests.items(), key=lambda item: item[1], reverse=True)]
    return jsonify({"points": requests_points})

@statistics_bp.route('/food/weight', methods=['GET'])
def get_weights_by_area():
    df = data_loader.get_data()
    area_weight = df.groupby("Area")["Weight"].sum()
    weight_points = [{"x": area, "y": value} for area, value in
                    sorted(area_weight.items(), key=lambda item: item[1], reverse=True)]
    return jsonify({"points": weight_points})

@statistics_bp.route('/dss/requests', methods=['GET'])
def get_requests_by_dss():
    df = data_loader.get_data()
    dss_requests = df.groupby("DSS")["Requests"].sum()
    request_points = [{"x": dss, "y": value} for dss, value in
                      sorted(dss_requests.items(), key=lambda item: item[1], reverse=True)]
    return jsonify({"points": request_points})


@statistics_bp.route('/dss/weight', methods=['GET'])
def get_weights_by_dss():
    df = data_loader.get_data()
    dss_weights = df.groupby("DSS")["Weight"].sum()
    weight_points = [{"x": dss, "y": value} for dss, value in
                     sorted(dss_weights.items(), key=lambda item: item[1], reverse=True)]
    return jsonify({"points": weight_points})
