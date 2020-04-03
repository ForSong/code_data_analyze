import pandas as pd

df = pd.read_csv("./dogNames2.csv")

# 显示头几行，默认为5
# print(df.head())
# 展示dataframe的概览
# print(df.info())
# int和float类型数据的均值中位数等数学特性
# print(df.describe)

# 对DataFrame中的数据进行排序
df = df.sort_values(by="Count_AnimalName", ascending=False)
print(df.head(10))

# 下面是pandas中取行或者列
# 注意：如果方括号写数组，表示取行，对行进行操作
# 如果方括号写字符串，表示取列索引，对列操作
print(df[:20])
print(df["Row_Labels"])

print(type(df[:20]))
# 注意这个是Series类型1
print(type(df["Row_Labels"]))
