# coding=utf-8

# 频数分布直方图:需要原始数据，如果是已经统计完成之后的数据不能绘制直方图
# 已经统计好的数据可以使用条形图来展示，因为无法使用hist这个方法
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

a = [123, 112, 131, 312, 342, 123, 141, 141, 133, 141]

# 注意取组距的时候的方式
# 计算组数
d = 6  # 组距
num_bin = (max(a) - min(a)) // d  # 组数
# 设置图形大小
plt.figure(figsize=(20, 8), dpi=50)
# 如果想画频率分布直方图的话，增加参数
# mormid 的意思就是是否为频率分布True的时候表示是
plt.hist(a, num_bin, normid=True)

# 设置x轴刻度
plt.xticks(range(min(a), max(a), d))
plt.grid(0.6)

plt.show()
