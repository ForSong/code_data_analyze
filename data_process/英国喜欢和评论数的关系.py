# 对于关系的图一般使用的是散点图
import numpy as np
from matplotlib import pyplot as plt

us_file_path = "./data/US_video_data_numbers.csv"
uk_file_path = "./data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path, delimiter=",",dtype="int",unpack=True)
# 载入文件并取评论行，最后一行 usecols = -1
# 也可以使用t_us_comments = t_us[:,-1]
t_uk = np.loadtxt(uk_file_path, delimiter=",", dtype="int")

# 选出喜欢数小于等于500000的数据
t_uk = t_uk[t_uk[:, 1] <= 500000]

t_uk_comment = t_uk[:, -1]
t_uk_like = t_uk[:, 1]

# 不能用下面的方式筛选，原因是这样会导致两个数据数量不对应
# t_uk_like[t_uk_like <= 500000]

plt.figure(figsize=(20, 8), dpi=60)
plt.scatter(t_uk_like, t_uk_comment)
plt.show()
