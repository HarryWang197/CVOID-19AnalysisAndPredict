#!/usr/bin/env python3
# @Time    : 2020/4/1 17:11
# @Author  : Harry Wang


def abs_values(a):
    if a > 0:
        return a
    elif a == 0:
        return 0
    else:
        return -x

x = int(input('请输入一个数:'))
print(abs_values(x))
