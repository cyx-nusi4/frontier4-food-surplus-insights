from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta

app = Flask(__name__)

# 1️⃣ **加载数据并确保格式正确**
def load_data(file_name):
    file_path = os.path.abspath(file_name)
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"CSV file '{file_name}' not found.")
    
    df = pd.read_csv(file_path, encoding="latin1")
    
    # 确保 'Date' 列转换为 datetime 格式
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Year-Month'] = df['Date'].dt.to_period("M")
    
    # 处理 'Weight' 列，去除 "KG" 并转换为数值
    df["Weight"] = pd.to_numeric(df["Weight"].astype(str).str.replace("KG", "", case=False), errors="coerce").fillna(0)
    
    return df


df_forecast = load_data("filtered_file.csv")

# 2️⃣ **训练线性回归模型**
# 2️⃣ **训练线性回归模型（使用所有数据）**
def train_model(df):
    if 'Date' not in df.columns or 'Weight' not in df.columns:
        raise ValueError("Dataset must contain 'Date' and 'Weight' columns.")

    # 计算 'Days'，从数据中的最早日期开始计算天数
    min_date = df['Date'].min()
    df['Days'] = (df['Date'] - min_date).dt.days
    print(df['Days'][:5])

    if df.empty:
        raise ValueError(" CSV!")

    # 处理缺失值
    df['Weight'] = df['Weight'].interpolate()

    X = df['Days'].values.reshape(-1, 1)
    print(X[:5])
    y = df['Weight'].values
    print(y[:5])

    # 检查数据是否为空
    if len(X) == 0 or len(y) == 0:
        raise ValueError("!")

    print(f"✅ 训练数据: {X.shape[0]} 行")

    # 训练模型
    model = LinearRegression()
    model.fit(X, y)
    return model

# 使用整个数据集训练
model = train_model(df_forecast)


# 3️⃣ **预测未来重量**
@app.route('/forecast/byWeight', methods=['GET'])
def predict_future_weight():
    days_ahead = request.args.get('duration', default=10, type=int)
    
    future_dates = [datetime.now() + timedelta(days=i) for i in range(days_ahead + 1)]
    future_days = np.array([(date - datetime(2024, 1, 1)).days for date in future_dates]).reshape(-1, 1)
    future_weights = model.predict(future_days)
    
    show_points = days_ahead <= 60  # 控制是否展示散点
    
    predictions = [
        {"x": date.strftime('%Y-%m-%d'), "y": weight, "show_point": show_points}
        for date, weight in zip(future_dates, future_weights)
    ]
    
    return jsonify({"points": predictions, "show_points": show_points})

# 4️⃣ **获取区域请求总数**
@app.route('/requests', methods=['GET'])
def get_requests_by_area():
    area_requests = df_forecast.groupby("Area")["Requests"].sum()
    requests_points = [{"x": area, "y": value} for area, value in sorted(area_requests.items(), key=lambda item: item[1], reverse=True)]
    return jsonify({"requests_points": requests_points})

# 5️⃣ **获取区域重量总数**
@app.route('/weights', methods=['GET'])
def get_weights_by_area():
    area_weight = df_forecast.groupby("Area")["Weight"].sum()
    weight_points = [{"x": area, "y": value} for area, value in sorted(area_weight.items(), key=lambda item: item[1], reverse=True)]
    return jsonify({"weight_points": weight_points})

# 6️⃣ **生成热力图数据**
area_location_dict = {
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

@app.route('/heatmap', methods=['GET'])
def generate_heatmap():
    start_date_str = request.args.get('startDate')
    end_date_str = request.args.get('endDate')

    if not start_date_str or not end_date_str:
        return jsonify({"error": "Please provide both startDate and endDate parameters"}), 400

    # 解析日期
    try:
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

    # 读取 CSV 数据
    file_path = os.path.abspath("filtered_file.csv")
    df = pd.read_csv(file_path)

    # 确保 'Area' 和 'Weight' 存在
    if 'Area' not in df.columns or 'Weight' not in df.columns:
        return jsonify({"error": "CSV must contain 'Area' and 'Weight' columns"}), 400

    # 解析 Date 列
    df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d', errors='coerce')
    print(f"✅ 数据时间范围: {df['Date'].min()} ~ {df['Date'].max()}")

    # 过滤日期范围
    df_filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
    print(f"✅ 过滤后数据行数: {df_filtered.shape[0]}")

    if df_filtered.empty:
        return jsonify({"error": "No data available for the selected date range"}), 400

    # 处理 Area 坐标
    df_filtered['Latitude'] = df_filtered['Area'].map(lambda x: area_location_dict.get(x, (None, None))[0])
    df_filtered['Longitude'] = df_filtered['Area'].map(lambda x: area_location_dict.get(x, (None, None))[1])

    # 检查未匹配的 Area
    unmatched_areas = df_filtered[df_filtered['Latitude'].isna()]['Area'].unique()
    if len(unmatched_areas) > 0:
        print(f"⚠️ 未匹配的区域: {unmatched_areas}")

    # 过滤掉无坐标的数据
    df_cleaned = df_filtered.dropna(subset=['Latitude', 'Longitude', 'Weight'])
    print(f"✅ 清理后数据行数: {df_cleaned.shape[0]}")

    # 生成热力图数据
    heat_data = [[row['Latitude'], row['Longitude'], row['Weight']] for index, row in df_cleaned.iterrows()]

    return jsonify({"heat_data": heat_data})

if __name__ == '__main__':
    app.run(debug=True, port=5002)
