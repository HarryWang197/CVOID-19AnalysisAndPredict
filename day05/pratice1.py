#!/usr/bin/env python3
# @Time    : 2020/4/6 16:04
# @Author  : Harry Wang

from pyecharts.charts import Map
from pyecharts import options as opts
import json
import requests
import time

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(time.time() * 1000)
data = json.loads(requests.get(url=url).json()['data'])
# 统计省份信息(34个省份 湖北 广东 河南 浙江 湖南 安徽....)
provinces_data = data['areaTree'][0]['children']
province_confirm_data = {}
for province_data in provinces_data:
    province_confirm_data[province_data["name"]] = province_data["total"]["confirm"]
print(province_confirm_data)

virus_map = Map()
virus_map.add('中国疫情地图', data_pair=province_confirm_data.items())
virus_map.set_global_opts(visualmap_opts=opts.VisualMapOpts(split_number=6,
                                                            is_piecewise=True,
                                                            pieces=[{"min": 1, "max": 9, "label": "1-9人", "color": "#ffefd7"},
                                                                    {"min": 10, "max": 99, "label": "10-99人", "color": "#ffd2a0"},
                                                                    {"min": 100, "max": 499, "label": "100-499人", "color": "#fe8664"},
                                                                    {"min": 500, "max": 999, "label": "500-999人", "color": "#e64b47"},
                                                                    {"min": 1000, "max": 9999, "label": "1000-9999人", "color": "#c91014"},
                                                                    {"min": 10000, "label": "10000人及以上", "color": "#9c0a0d"}]),
                          title_opts=opts.TitleOpts(title="中国确认病例地图"))
virus_map.render()
