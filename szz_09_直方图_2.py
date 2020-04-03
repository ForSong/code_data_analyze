from matplotlib import pyplot as plt
from matplotlib import font_manager

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]  # 时间段
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]  # 组距
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 824, 613, 215, 47]  # 每个时间段对应数据

# print(len(interval),len(width),len(quantity))

# width 默认值是0.8 每个条之间有间隙， 如果将数字改为1的话各个条就会连起来
plt.bar(range(len(quantity)), quantity, width=1)

# 设置x轴的刻度
# 注意最后一个值如果没有的话要增加一个数，然后再将刻度也加上
_x = [i - 0.5 for i in range(len(quantity) + 1)]  # 这里加1
_xtick_label = interval + [150]  # 这里加上最后一个数据的跨度
plt.xticks(range(len(quantity)), _xtick_label)

plt.xticks(_x, _xtick_label)

plt.show()
