# -*- coding: UTF-8 -*-
# Filename : dic_merge
# author by : yanbing

"""
将两个字典融合成一个
"""

# 两个字典
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
"""
方法一：运用updata方法，第二个参数合并第一个参数，注意的是update没有返回值
"""
def Merge(dict1, dict2):
    return (dict1.update(dict2))

# 返回  None
print(Merge(dict1, dict2))

# dict2 合并了 dict1
print(dict1)

"""
方法二：使用 **，函数将参数以字典的形式导入
"""
def Merge(dict2, dict1):
    res = {**dict1, **dict2}
    return res

# 两个字典
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)