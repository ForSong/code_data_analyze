import numpy as np
from matplotlib import pyplot as plt

us_file_path = "./data/US_video_data_numbers.csv"
uk_file_path = "./data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path, delimiter=",",dtype="int",unpack=True)
# 载入文件并取评论行，最后一行 usecols = -1
# 也可以使用t_us_comments = t_us[:,-1]
t_us_comments = np.loadtxt(us_file_path, delimiter=",", dtype="int", usecols=-1)

# 将其中比5000小的数据选择出来
t_us_comments = t_us_comments[t_us_comments <= 5000]

print(t_us_comments.max(), t_us_comments.min())

d = 50

bin_num = (t_us_comments.max() - t_us_comments.min()) // d


# 绘图
# 设置图形大小
plt.figure(figsize=(20, 8), dpi=60)
# 如果将bin_num 刚换为列表将会解决bin_num除不尽的偏移问题
plt.hist(t_us_comments, bin_num)
plt.show()
