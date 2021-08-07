# - * - coding: UTF - 8 -*-
# Filename : equation_solution
# author by : yanbing
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0
# 导入 cmath(复杂数学运算) 模块
import cmath

a = float(input('输入 a: '))
b = float(input('输入 b: '))
c = float(input('输入 c: '))
# 计算
d = (b ** 2) - (4 * a * c)
# 两种求解方式
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print(f'结果为 {sol1} 和 {sol2}')
