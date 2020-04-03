import pandas as pd
import numpy as np

s = pd.Series([1, 2, 3, 53, 13, 52, 11, 3])

# print(s)
# print(type(s))

t2 = pd.Series([321, 12, 3, 12, 4], index=list("abcde"))
# print(t2)

# print(list("abc"))

temp_dict = {"name": "xiaohong", "age": 13, "tel": 10086}
t3 = pd.Series(temp_dict)
# print(t3)
# print(t3.dtype)

# 取连续的两行
# prinR

# 取不连续的两行
# print(t3[0:2])

# 用索引取值
# print(t3[["age", "name"]])

for i in t3.index:
    print(i)

# print(t3.index)
#
# print(len(t3))
#
# print(list(t3))
#
# print(list(t3.index)[:2])
t = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list("abc"), columns=list("wxyz"))
# print(t)
d1 = {"name": ["xiaoming", "xiaogang"], "age": [20, 23], "tel": [10010, 12345]}

print(pd.DataFrame(d1))

d2 = [{"name": "xiaohong", "age": 23, "tel": 10000}, {"name": "xiaogang", "tel": 10000}, {"name": "xiaoli"}]

print(pd.DataFrame(d2))
