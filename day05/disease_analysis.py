#!/usr/bin/env python3
# @Time    : 2020/4/3 17:03
# @Author  : Harry Wang

import matplotlib.pyplot as plt
import requests
import time
import json
from datetime import datetime

from matplotlib.dates import DateFormatter
from matplotlib.ticker import MultipleLocator

plt.rcParams['font.sans-serif'] = ['SimHei']

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other&callback=&_ = %d' % int(time.time() * 1000)
response = requests.get(url)

response_json = response.json()
data = response_json['data']
# print(data)

data_dict = json.loads(data)
# print(data_dict)


day_list = []

confirm_list = []
heal_list = []
dead_list = []

daily_history = data_dict['dailyHistory']

for item in daily_history:
    print(item)
    month, day = item['date'].split('.')
    date = '2020-%s-%s' % (month, day)
    date_format = datetime.strptime(date, '%Y-%m-%d')
    day_list.append(date_format)

    dead_list.append(item['hubei']['dead'])
    heal_list.append(item['hubei']['heal'])
    confirm_list.append(item['hubei']['nowConfirm'])

plt.plot(day_list, confirm_list, color='red', label='确诊')
plt.plot(day_list, heal_list, color='green', label='治愈')
plt.plot(day_list, dead_list, color='grey', label='死亡')

# 显示图例，指定位置，防止图片被覆盖
plt.legend(loc='upper left')

# 显示网格
plt.grid(linestyle=':')

# 日期去掉年
plt.gca().xaxis.set_major_formatter(DateFormatter('%m-%d'))

# 设置x轴间距
xmajorLocator = MultipleLocator(7)
plt.gca().xaxis.set_major_locator(xmajorLocator)


plt.xlabel('日期')
plt.ylabel('人数')
plt.title('湖北确诊/死亡/治愈趋势')

plt.show()
