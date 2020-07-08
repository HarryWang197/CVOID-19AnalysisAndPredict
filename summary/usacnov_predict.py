#!/usr/bin/env python3
# @Time    : 2020/4/11 16:34
# @Author  : Harry Wang
import numpy as np

# x轴位时间
# y轴位预测数
from summary.fitting_parameters import logistic_function, optimal_p0

x_data = np.arange(0, 100)
y_data = logistic_function(x_data, optimal_p0)
y_data = y_data.astype('int64')
# print(y_data)