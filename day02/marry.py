#!/usr/bin/env python3
# @Time    : 2020/3/31 16:24
# @Author  : Harry Wang

age = input('请输入年龄(范围：0-100):')
appearance = input('请输入颜值（范围：0-100):')
money = input('请输入存款(上不封顶):')

age = int(age)
appearance = int(appearance)
money = int(money)

if age < 25 and appearance > 90 and money > 1000000:
    print('我要嫁给你！')
elif age < 25 or appearance > 90 or money > 1000000:
    print('哎！嫁了吧！')
else:
    print('不嫁！')

