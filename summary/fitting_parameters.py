#!/usr/bin/env python3
# @Time    : 2020/4/10 11:32
# @Author  : Harry Wang
import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import mean_squared_error

from summary.get_history_datas import xdata, ydata

parameter_K = None
parameter_r = None

def logistic_function(t, P0):
    exp_r = np.exp(parameter_r * t)
    return parameter_K * P0 * exp_r / (parameter_K + P0 * (exp_r - 1))

k_range = np.arange(500000, 1000000, 5000)
r_range = np.arange(0, 1, 0.01)

loss = float('inf')

optimal_k = None
optimal_p0 = None
optimal_r = None

i = 0
# 从k_range和r_range中找到最优的k和r
# 如何才算最优解？均方误差（机器学习库metrics中的mean_squared_error函数）
for k_ in k_range:
    for r_ in r_range:
        # 将最优解赋值给logistics函数中的参数
        parameter_K = k_
        parameter_r = r_
        # popt：返回logistic函数中最优的参数p0
        popt, pcov = curve_fit(logistic_function, xdata, ydata)

        # y_true:y轴真实值
        # y_pred:预测值，logistic方程返回的值
        # ydata:真实的值；logistic_function(xdata, popt):预测的值。两个值做均方误差得到的误差值
        loss_= mean_squared_error(ydata, logistic_function(xdata, popt))
        # 根据最小误差得到的三个参数也是最小的
        if loss_ < loss:
            loss = loss_
            optimal_k = k_
            optimal_r = r_
            optimal_p0 = popt

        i += 1
    # 第一个'▎' * int(10 * i / len(k_range) / len(r_range))是进度条
    # 第二个int(100 * i / len(k_range) / len(r_range))是百分数
    print('\r拟合进度：{0}{1}%'.format('▌' * int(10 * i / len(k_range) / len(r_range)), int(100 * i / len(k_range) / len(r_range))), end = '')

# print('\noptimal_K: ', optimal_k)
# print('optimal_r: ', optimal_r)
# print('optimal_P0: ', optimal_p0)

parameter_K = optimal_k
parameter_r = optimal_r