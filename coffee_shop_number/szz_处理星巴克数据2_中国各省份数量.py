import pandas as pd

# 统计中国每个省的店铺数量

# 导入数据
file_path = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)

# 根据列索引找到中国的数据
china_data = df[df["Country"] == "CN"]
print(china_data)
print(china_data.info())

# 将得到的数据分组
# Groupby 对数据进行分组
# grouped = china_data.groupby(by="State/Province").count()
# 如果是直接对df进行分组的话在by=的后面就不用再写df[]可以直接写列的名称即可
# # 所以既可以先分组在选所需要的列，也可以先取出所需要的列，在对列进行分组，主要区别是by=的后面是否需要df[]
# # 如果想要返回DataFrame只需要
# grouped2 = df["Brand"].groupby(by=[df["Country"], df["State/Province"]]).count()
# 下面这种方式是放回DataFrame
grouped1 = df[["Brand"]].groupby(by=[df["Country"], df["State/Province"]])[["Brand"]].count()
# grouped3 = df.groupby(by=[df["Country"],df["State/Province"]]).count()["Brand"]
# grouped4 = df.groupby(by=[df["Country"],df["State/Province"]])["Brand"].count()
# print(grouped2)
# # 虽然有三列，但是仍然是Series类型，前两个都是索引
# print(type(grouped2))
# print(type(grouped))

# 索引的方法和属性

print(grouped1.index)
# 对已有的DataFrame的索引进行赋值df.index=["a","b"]
# 重新设置df.reindex(["a","f"])取原来的a行和f行赋值给新的DataFrame如果没有对应的索引，那么那一行的数据就会是NaN
# set_index方法是将当前的某一列作为索引，如df.set_index("a",drop=False)这里如果
