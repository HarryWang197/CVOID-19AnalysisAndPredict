#!/usr/bin/env python3
# @Time    : 2020/3/31 16:46
# @Author  : Harry Wang

arthur_life = 150
arthur_attack = 12
ake_life = 100
ake_attack = 15

while arthur_life > 0 and ake_life > 0:
    arthur_life -= ake_attack
    ake_life -= arthur_attack
if arthur_life > 0 and ake_life < 0:
    print('亚瑟胜利！')
elif arthur_life < 0 and ake_life > 0:
    print('阿珂胜利！')
elif arthur_life < 0 and ake_life < 0:
    print('同归于尽！')
else:
    print('打平！')
