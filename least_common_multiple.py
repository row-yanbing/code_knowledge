# -*- codiyng: UTF-8 -*-
# Filename : least_common_multiple
# author by : yanbing

# 定义函数
def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm_num = greater
            break
        greater += 1
    return lcm_num


# 获取用户输入
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print(num1, "和", num2, "的最小公倍数为", lcm(num1, num2))
