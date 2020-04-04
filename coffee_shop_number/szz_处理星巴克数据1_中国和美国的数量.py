import pandas as pd
import numpy as np

file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)
# print(df.head(1))
print(df.info())

# grouped = df.groupby(by="Country")
# print(grouped)

# DataFrameGroupBy 1. 可以进行遍历 2. 也可以调用聚合方法 3. 也可以取平均数和中位数
# 1. 进行遍历
# for i, j in grouped:
#     print(i)
#     print("-" * 100)
#     print(j,type(j))
#     print("*" * 100)
# var = df[df["Country"] == "US"]
# print(var)
# 2. 调用聚合方法
# country_count = grouped["Brand"].count()
# # 取索引
# # 统计不同国家的行吧可星巴克数量
# print(country_count["US"])
# print(country_count["CN"])

# 统计中国每个省份的店铺的数量
china_data = df[df["Country"] == "CN"]
grouped = china_data.groupby(by="State/Province").count()["Brand"]
print(grouped)
