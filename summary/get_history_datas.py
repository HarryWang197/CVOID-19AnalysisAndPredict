#!/usr/bin/env python3
# @Time    : 2020/4/10 11:04
# @Author  : Harry Wang
import json
import numpy as np

import requests
url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country=%E7%BE%8E%E5%9B%BD&'

response = requests.get(url)
USA_datas = response.json()['data']

print(USA_datas)

x_now_date = []
ydata = []
# x_data,y_data是拟合函数中需要的参数，必须是真实的数据用于对比要预测的数据
# y_data表示y轴上真实的数据（即确诊人数）

for item in USA_datas:
    x_now_date.append(item['date'])
    ydata.append(item['confirm'])

# xdata表示x轴上的数据（即日期）。注意：xdata必须是整数
xdata = np.arange(0, len(ydata))


