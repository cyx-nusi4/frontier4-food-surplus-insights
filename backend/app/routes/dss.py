from flask import Blueprint, jsonify, request
from datetime import datetime
from app.extensions import data_loader
import pandas as pd
import re

dss_bp = Blueprint('dss', __name__)

MAX_DSS = 50
MAX_AREAS = 20
DEFAULT_START = "2024-01-01"
DEFAULT_END = "2024-12-31"

def filter_dataframe(df, start_date_str=None, end_date_str=None, area_str=None):
    try:
        start_date = datetime.strptime(start_date_str or DEFAULT_START, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str or DEFAULT_END, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD")

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    if area_str:
        try:
            pattern = re.compile(re.escape(area_str), re.IGNORECASE)
            df = df[df['Area'].apply(lambda x: bool(pattern.search(str(x))))]
        except re.error as e:
            raise ValueError(f"Invalid area pattern: {e}")

    return df
""" DSS 权重分布 """
@dss_bp.route('/dss/weight-distribution', methods=['GET'])
def dss_weight_distribution():
    df = data_loader.get_data()

    try:
        df = filter_dataframe(
            df,
            request.args.get('startDate'),
            request.args.get('endDate'),
            request.args.get('area')
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    top_dss = (
        df.groupby("DSS")["Weight"]
        .sum()
        .sort_values(ascending=False)
        .head(MAX_DSS)
    )

    data = [{"dss": dss, "weight": float(weight)} for dss, weight in top_dss.items()]
    return jsonify({"data": data})
""" DSS 请求量分布 """
@dss_bp.route('/dss/request-distribution', methods=['GET'])
def dss_request_distribution():
    df = data_loader.get_data()

    try:
        df = filter_dataframe(
            df,
            request.args.get('startDate'),
            request.args.get('endDate'),
            request.args.get('area')
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    top_dss = (
        df.groupby("DSS")["Requests"]
        .sum()
        .sort_values(ascending=False)
        .head(MAX_DSS)
    )

    data = [{"dss": dss, "requests": int(requests)} for dss, requests in top_dss.items()]
    return jsonify({"data": data})
    
""" DSS区域数量分布（唯一 DSS 计数） """
@dss_bp.route('/area/dss-distribution', methods=['GET'])
def area_dss_distribution():
    df = data_loader.get_data()
    try:
        df = filter_dataframe(
            df,
            request.args.get('startDate'),
            request.args.get('endDate'),
            request.args.get('area')
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    # 去重
    df_unique = df.drop_duplicates(subset=["Area", "DSS"])
    # 统计唯一 DSS 的数量
    area_counts = (
        df_unique["Area"]
        .value_counts()
        .sort_values(ascending=False)
        .head(MAX_AREAS)
    )

    data = [{"area": area, "count": int(count)} for area, count in area_counts.items()]
    return jsonify({"data": data})


""" DSS时间分布 """
@dss_bp.route('/dss/time-trend', methods=['GET'])
def dss_time_trend():
    df = data_loader.get_data()

    try:
        df = filter_dataframe(
            df,
            request.args.get('startDate'),
            request.args.get('endDate'),
            request.args.get('area')
        )
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    time_series = df.set_index('Date')['DSS'].resample('M').nunique()

    data = [{"date": date.strftime("%Y-%m"), "count": int(count)} for date, count in time_series.items()]
    return jsonify({"data": data})
