#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Filename : fib_nums
# author by : yanbing

def fib(n):
    a, b = 0, 1
    t = 1
    fib_nums = []
    while t <= n:
        a, b = b, a+b
        t += 1
        fib_nums.append(a)
    return fib_nums


print(fib(10))  # 取值范围可以任意
