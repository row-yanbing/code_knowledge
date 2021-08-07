# -*- coding: UTF-8 -*-

# Filename : num_sqrt
# author by : yanbing

# 计算实数和复数平方根
# 导入复数数学模块

import cmath

num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print(f'{num} 的平方根为 {num_sqrt}')
