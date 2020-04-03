import numpy as np
import random

t1 = np.array([1, 2, 3])
print(t1)
print(type(t1))

t2 = np.array(range(10))

print(t2)
print(type(t2))

# np.arange 的作用和t2 相同可以快速生成到某个数字之间的数字
t3 = np.arange(4, 10, 2)
print(t3)
print(type(t3))

print(t3.dtype)

# numpy中的数据类型
t4 = np.array(range(1, 4), dtype="i1")
print(t4, t4.dtype)

# numpy 中的bool类型
t5 = np.array([1, 1, 0, 1, 0, 1], dtype=bool)
print(t5)
print(t5.dtype)

# 调整数据类型
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

# numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)

# 取两位小数
t8 = np.round(t7, 2)
print(t8)
# shape里面有几个数字就是几维的数字
t6 = np.arange(100, 124).reshape((4, 6))

print(t6)

t5 = np.arange(10, 34).reshape((4, 6))
print(t6 + t5)

