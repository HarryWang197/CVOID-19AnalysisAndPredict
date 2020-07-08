#!/usr/bin/env python3
# @Time    : 2020/4/2 9:25
# @Author  : Harry Wang
import json

import requests
import time
import matplotlib.pyplot as plt


url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_ = %d' % int(time.time() * 1000)


response = requests.get(url)

response_json = response.json()
print(response_json)

data = response_json['data']
print(data)
data_dict = json.loads(data)
# print(data_dict)
# 获取到数据并转换成字典

province_list = data_dict['areaTree'][0]['children']

province_name = []
province_confirm = []

for province in province_list:
    province_name.append(province['name'])
    province_confirm.append(province['total']['confirm'])

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.bar(province_name, province_confirm)

plt.xlim(0, 9)
plt.xlabel = '省份'
plt.ylabel = '确诊人数'
plt.title = '全国各个省份新冠肺炎疫情感染确诊一览表'

plt.show()
# city_name = []
# city_confirm = []
#
# for city in henan_cities:
#     city_name = city['name']
#     city_confirm = city['total']['confirm']
