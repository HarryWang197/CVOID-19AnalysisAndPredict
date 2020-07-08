#!/usr/bin/env python3
# @Time    : 2020/3/31 16:52
# @Author  : Harry Wang
starts = '王一博 李现 杨紫 肖战 易烊千玺 关晓彤 李现 杨紫 肖战 易烊千玺 王一博 关晓彤 肖战 李现'
name = starts.split(' ')
print(name)
count = 0
for i in name:
    if i == '李现':
        count += 1
print(count)

