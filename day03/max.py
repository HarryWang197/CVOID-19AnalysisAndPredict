#!/usr/bin/env python3
# @Time    : 2020/4/1 16:59
# @Author  : Harry Wang

x = input('输入一个数:')
y = input('再输入一个数:')


def max_number(a, b):
    if a > b:
        return a
    else:
        return b

print('最大数为:'+max_number(x, y))
