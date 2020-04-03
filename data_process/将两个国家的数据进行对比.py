import numpy as np

# 加载国家数据
uk_data = "./data/GB_video_data_numbers.csv"
us_data = "./data/US_video_data_numbers.csv"
t_uk = np.loadtxt(uk_data, delimiter=",", dtype=int)
t_us = np.loadtxt(us_data, delimiter=",", dtype=int)

# 添加国家信息
# 构造全为0的数据
zeros_data = np.zeros((t_us.shape[0], 1)).astype(int)

# 构造全为1的数据
ones_data = np.ones((t_uk.shape[0], 1)).astype(int)

# 数据拼接,分别添加1列全为0，1的数据
t_us = np.hstack((t_us, zeros_data))
t_uk = np.hstack((t_uk, ones_data))

# 拼接两组数据
final_data = np.vstack((t_us, t_uk))
print(final_data)
