# coding=utf-8
import random

from matplotlib import pyplot as plt

x = range(2, 28, 2)
y = [15, 13, 14, 5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

# 设置图片大小
fig = plt.figure(figsize=(30, 10), dpi=80)
# 保存到本地
# 绘图
_xtick_labels = [i / 2 for i in range(2, 49)]

# ！！！ 设置x轴的刻度
plt.xticks(_xtick_labels[::3], fontsize=10)  # 取步长
# ！！！ 设置y周的刻度
plt.yticks(range(min(y), max(y) + 1))  # 注意右边是取不到了
plt.plot(x, y)
# 注意保存要在绘图之后 也就是在plot之后
plt.savefig("./p2.png")  # 保存svg的话就把后缀改掉就可以了
# 调整刻度

a = [random.randint(20, 35) for i in range(120)]
print(a)

# 设置x轴的刻度
# 标出特殊的点
# 线条特性
# 增加水印


# 展示图形
plt.show()
