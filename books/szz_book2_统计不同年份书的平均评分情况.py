import pandas as pd
from matplotlib import pyplot as plt

# 统计不同年份的平均评分情况
file_path = "./books.csv"
df = pd.read_csv(file_path)
# 利用布尔索引，取出不为空的值
data1 = df[pd.notnull(df["original_publication_year"])]

# 将评分按照年份分类，并求平均值
grouped = data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()
print(grouped)

_x = grouped.index
_y = grouped.values

# 画图
plt.figure(figsize=(20, 8), dpi=50)
plt.plot(range(len(_x)), _y)
plt.xticks(list(range(len(_x)))[::10], _x[::10].astype(int))
plt.show()
