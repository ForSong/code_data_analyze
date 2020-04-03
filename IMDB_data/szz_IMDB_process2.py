import pandas as pd
from matplotlib import pyplot as plt

file_path = "IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

# print(df.info())
# print(df.head(1))


# Rating, runtime 分布情况，根据上面的结果，一共有100行数据，而且这两项也有一千行数据
# 选择图形，直方图
# 准备数据
runtime_data = df["Runtime (Minutes)"].values

max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算组数
num_bin = (max_runtime - min_runtime) // 5

# 设置图形的大小
plt.figure(figsize=(20, 8), dpi=60)
plt.hist(runtime_data, num_bin)

plt.xticks(range(min_runtime, max_runtime+5,5))
plt.show()
