from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")
y_3 = [19, 17, 17, 18, 12, 15, 13, 18, 16, 16, 15, 14, 13, 14, 12, 32, 32, 12, 12, 32, 23, 23, 12, 43, 23, 12, 32, 12,
       32, 12]
y_10 = [20, 10, 14, 16, 36, 1, 23, 14, 13, 14, 12, 14, 14, 12, 13, 18, 16, 16, 15, 14, 13, 14, 12, 32, 32, 12, 12, 32,
        23, 23, 12]
# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

# 这里是要显示出来的刻度有哪些，然后对应要显示出来的刻度，每个刻度上有一个对应的标签值
# 要显示的刻度的数量和y的数量以及标签的数量应该是一致的
# 如果你想让他变的稀疏，那么就对要显示出来的个数取步长，然后将2对应的标签改为1再对应y即可
# 如果想要变得密集，那么就
x_3 = range(0, 60, 2)
x_10 = range(64, 125, 2)
# 设置x轴刻度
_x = list(x_3) + list(x_10)
_xtick_labels = ["3月{}日".format(int((i + 2) / 2)) for i in x_3]
_xtick_labels += ["10月{}日".format(int((i - 62) / 2)) for i in x_10]
plt.xticks(_x, _xtick_labels, fontproperties=my_font, rotation=45)
# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)
plt.title("三月份和十月份气温", fontproperties=my_font)
# 添加图例第一步

# 使用scatter绘制散点图，和之前绘制折线图的唯一区别
plt.scatter(list(x_3), y_3, label="3月份")
plt.scatter(x_10, y_10, label="10月份")
# 添加图例第二步
plt.legend(loc='upper left', prop=my_font)
plt.show()

