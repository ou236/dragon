import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


df = pd.read_csv(r'D:\streamlit_env\student_data_adjusted_rounded.csv') # 替换为你的数据文件路径


features = ["每周学习时长（小时）", "上课出勤率", "期中考试分数", "作业完成率"]
X = df[features]
y = df["期末考试分数"]


model = LinearRegression()
model.fit(X, y)


joblib.dump(model, "score_predictor.pkl")

print("模型训练完成并保存为 score_predictor.pkl")
