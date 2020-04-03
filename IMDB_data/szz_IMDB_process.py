import pandas as pd
import numpy as np

file_path = "IMDB-Movie-Data.csv"
df = pd.read_csv(file_path)

# print(df.info())

# print(df.head(1))

# 获取平均评分
# print(df["Rating"].mean())

# 导演的人数
# print(len(set(df["Director"].tolist())))
# unique函数返回一个列表
# print(len(df["Director"].unique()))

# 获取演员的人数
temp_actors_list = df["Actors"].str.split(", ").tolist()
print(temp_actors_list)
# 大列表套小列表的时候统计元素个数的方法,使用两次循环
actor_list = [i for j in temp_actors_list for i in j]

actor_name = len(set(actor_list))
print(actor_name)
