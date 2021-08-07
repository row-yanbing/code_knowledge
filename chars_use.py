# -*- codiyng: UTF-8 -*-
# Filename : chars_use
# author by : yanbing

# 测试实例一
print("测试实例一")
str1 = "runoob.com"
print(str1.isalnum()) # 判断所有字符都是数字或者字母
print(str1.isalpha()) # 判断所有字符都是字母
print(str1.isdigit()) # 判断所有字符都是数字
print(str1.islower()) # 判断所有字符都是小写
print(str1.isupper()) # 判断所有字符都是大写
print(str1.istitle()) # 判断所有单词都是首字母大写，像标题
print(str1.isspace()) # 判断所有字符都是空白字符、\t、\n、\r

# 测试实例二
print("测试实例二")
str2 = "www.rUnoob.com"
print(str2.upper())          # 把所有字符中的小写字母转换成大写字母
print(str2.lower())          # 把所有字符中的大写字母转换成小写字母
print(str2.capitalize())     # 把第一个字母转化为大写字母，其余小写
print(str2.title())          # 把每个单词的第一个字母转化为大写，其余小写