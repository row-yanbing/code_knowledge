# -*- coding: UTF-8 -*-
# Filename : dic_remove
# author by : yanbing

"""
移除字典点键值(key/value)对
"""
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

"""
方法一、利用del移除
"""
# 输出原始的字典
print("字典移除前 : " + str(test_dict))
# 使用 del 移除 Zhihu
del test_dict['Zhihu']
# 输出移除后的字典
print("字典移除后 : " + str(test_dict))
# 移除没有的 key 会报错
# del test_dict['Baidu']

test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
"""
方法二、利用pop移除
"""
# 使用 pop 移除 Zhihu
removed_value = test_dict.pop('Zhihu')
# 输出移除后的字典
print("字典移除后 : " + str(test_dict))
print("移除的 key 对应的 value 为 : " + str(removed_value))
print('\r')

test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
"""
方法三、利用items（）移除
"""
# 输出原始的字典
print("字典移除前 : " + str(test_dict))
# 使用 pop 移除 Zhihu
new_dict = {key: val for key, val in test_dict.items() if key != 'Zhihu'}
# 输出移除后的字典
print("字典移除后 : " + str(new_dict))
