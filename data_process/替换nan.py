# 将一个数组中的nan值替换为该列的平均值
# 布尔索引， 取行取列， 切片操作
import numpy as np


# t1.shape[]是多维数组，0 为行 1 为列 2 为块
# 这里遍历每一列
def file_ndarray(t1):
    for i in range(t1.shape[1]):
        temp_col = t1[:, i]  # 当前列
        # 判断是否有nan，将np.count_nonzero()方法和 t != t 相结合（利用了nan不等于自身的特点）
        nan_num = np.count_nonzero(temp_col != temp_col)
        print(nan_num)
        if nan_num != 0:
            # 取出当前列中不为nan的nan的值组成的列表
            temp_not_nan_col = temp_col[temp_col == temp_col]
            # 计算他们的平均值，并将这个平均值放如nan这个位置中
            #   np.isnan(temp_col)返回了一个索引，对应的是nan位置的索引
            #   这里也可以用 temp_col != temp_col 代替
            temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()

    return t1


if __name__ == '__main__':
    t1 = np.arange(24).reshape((4, 6)).astype("float")

    # 将第二行的第3列之后的内容替换为nan
    # 如果单独这样写的话会报错，需要将t1改成浮点类型
    t1[1, 2:] = np.nan
    print(t1)

    t1 = file_ndarray(t1)
    print(t1)
