# -*- coding: UTF-8 -*-

# Filename : var_trans
# author by : yanbing

# 用户输入

x = input('输入 x 值: ')
y = input('输入 y 值: ')

# 不使用临时变量
x, y = y, x

print(f'交换后 x,y 的值为:x= {x},y= {y}')
