#!/usr/bin/env python3
# @Time    : 2020/3/31 17:08
# @Author  : Harry Wang
infos = {'哈登':'123456', '詹姆斯':'456789', '字母哥':'666666'}

name = input('用户名：')
password = input('密码：')

if name == infos.keys() and password == infos.values():
    print('登录成功！')
elif name == infos.keys() and password != infos.values():
    print('密码不正确！')
elif name != infos.keys():
    print('用户不存在！')
# for i in infos.keys():
#     for j in infos.values():
#          print(i)
#          print(j)
#     if name == i and password == j:
#         print('登录成功！')
#     elif name == i and password != j:
#         print('密码不正确！')
#     else:
#         print('用户不存在！')
#
