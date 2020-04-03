import random

from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

# windows 和 linux 下设置字体
# 方式一
# font = {'family': 'Microsoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc("font", **font)
# 方式二
# matplotlib.rc("font", family='Microsoft YaHei',weight='blod')
# 这种方式和上面的方式其实是一样，**font将上面的字典形式转换为下面的键值对

# 通用的方式，肯定是可以的 mac中直接command加空格搜索字体，win中直接在开始中搜索
# 将字体加载进来，注意要在x轴那里也要修改
# plt.xticks(_x[::3], _xtick_labels[::3], rotation=45,fontproperties=my_font)
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

# 问题：x轴显示的时间是数字而不是时间
# 将x轴装换为字符串
plt.figure(figsize=(20, 10), dpi=80)
# 调整x轴的刻度
# 这里要做的事情就是，给每个x轴上面对应的位置找一个相对应的中文标签。
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
print(_xtick_labels)
# list(x)是前置类型转换，因为range()是不能设置步长的
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)  # rotation是旋转的角度
# 给x轴和y轴添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title("十点到十二点每分钟的气温变化情况",fontproperties=my_font)
plt.plot(x, y)
plt.show()
