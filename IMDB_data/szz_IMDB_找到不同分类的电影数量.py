import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 将文件导入
file_path = "IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

# 统计分类的列表
temp_list = df["Genre"].str.split(",").tolist()  # 将某一列边成 [[],[],[]]这种形式
# print(temp_list)

# 去重并且列表化
genre_list = list(set([i for j in temp_list for i in j]))
# print(temp_list)

# 构造全为0的分类列表
# | A |  B | C |
# | 0 |  0 | 0 |
# | 0 |  0 | 0 |
# | 0 |  0 | 0 |
# 例如上面这个表格，每一行代表一个电影对应的分类，要想知道某个分类对应的总的电影数量，只需要对列进行求和即可
zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
# print(zeros_df)

# 给每个电影出现的分类位置赋值1
for i in range(df.shape[0]):
    zeros_df.loc[i, temp_list[i]] = 1

# 统计每个分类的电影的数量和
genre_count = zeros_df.sum(axis=0)
# print(genre_count)

# 对结果进行排序
genre_count = genre_count.sort_values()
print(genre_count)

_x = genre_count.index
_y = genre_count.values
# 绘图
plt.figure(figsize=(20, 8), dpi=40)

plt.bar(range(len(_x)),_y)

plt.xticks(range(len(_x)), _x)
plt.show()
