import pandas as pd
from matplotlib import pyplot as plt

# 统计不同年份数的数量
file_path = "./books.csv"
df = pd.read_csv(file_path)
# 利用布尔索引，取出不为空的值
data1 = df[pd.notnull(df["original_publication_year"])]

grouped = data1.groupby(by="original_publication_year").count()["title"]
values = grouped.sort_values(ascending=False).head(10)

_x = values.index
_y = values.values

plt.figure(figsize=(20, 8), dpi=40)
plt.bar(range(len(_x)), _y)

plt.xticks(range(len(_x)), _x)
plt.show()
