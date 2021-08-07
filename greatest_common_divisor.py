# -*- codiyng: UTF-8 -*-
# Filename : greatest_common_divisor
# author by : yanbing

def gcd(a, b):
    if a == 0:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


print(gcd(54, 24))
