# -*- coding: UTF-8 -*-

# Filename : chars_is_num
# author by : yanbing

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# 测试字符串和数字
print(is_number('foo'))  # False
print(is_number('-1.37'))  # True
print(is_number('1e3'))  # True
