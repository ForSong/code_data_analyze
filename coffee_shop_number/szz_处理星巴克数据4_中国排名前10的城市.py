import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)
df = df[df["Country"] == "CN"]

# 使用matplotlib呈现出店铺总数排名前10的国家
# 准备数据
data1 = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:25]

# 设置坐标
_x = data1.index
_y = data1.values

# 画图
plt.figure(figsize=(20, 10), dpi=60)
# plt.bar(range(len(_x)), _y)
plt.barh(range(len(_x)), _y, height=0.3, color="orange")
plt.yticks(range(len(_x)), _x, fontproperties=my_font)

plt.show()
