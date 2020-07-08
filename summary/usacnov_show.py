#!/usr/bin/env python3
# @Time    : 2020/4/11 16:54
# @Author  : Harry Wang

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

from summary.get_history_datas import ydata, USA_datas, x_now_date
from summary.usacnov_predict import y_data
import datetime as dt

month, day = USA_datas[0]['date'].split('.')
first_day = dt.datetime.strptime('2020-' + month + '-' + day, '%Y-%m-%d')
x_date = [(first_day + (dt.timedelta(days=i))).strftime("%m-%d") for i in range(100)]
# for day in x_data:
#     x_date = [(first_day +(dt.timedelta(days=day)).strftime('%m-%d'))]

plt.rcParams['font.sans-serif'] = ['SimHei']

# 设置画布大小及分辨率
plt.figure(figsize=(12, 6), dpi=300)

plt.plot(x_date, y_data, color='red', label='预测确诊')
plt.scatter(x_now_date, ydata, s=40, color='green', label='现有确诊')

# 显示图例，指定位置，防止图片被覆盖
plt.legend(loc='upper left')

# 显示网格
plt.grid(linestyle=':')

plt.xticks(rotation=60)

plt.ylabel('确诊人数')
plt.title('美国新冠疫情预测/确诊对比一览表')
plt.savefig('usa_predict.png', dpi=200)

plt.show()
