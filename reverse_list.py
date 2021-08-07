# -*- coding: UTF-8 -*-
# Filename : reverse_list
# author by : yanbing

"""
定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
以下演示了将数组的前面两个元素放到数组后面。
原始数组:
1,2,3,4,5,6,7
翻转后数组：
3,4,5,6,7,1,2
"""
######翻转数组

# 方法一：利用队列方法实现
def reverse_array(arr, d, n):
    if d >= n:
        print("参数大小无效")
        return
    for i in range(0, d):
        temp = arr[0]
        arr.pop(0)
        arr.append(temp)


arr1 = [1, 2, 3, 4, 5, 6, 7]
print("old:", arr1)
reverse_array(arr1, 2, len(arr1))
print("new:", arr1)


# 方法二：利用列表截取和拼接实现
def re_list(arr, d):
    arr = arr[d:]+arr[:d]
    return arr


arr1 = [1, 2, 3, 4, 5, 6, 7]
print('翻转前：')
print(arr1)
print('翻转后')
print(re_list(arr1, 2))
