# -*- coding: UTF-8 -*-
# Filename : dic_sort
# author by : yanbing

"""
按键(key)或值(value)对字典进行排序
"""


def dictionairy():
    # 声明字典

    key_value = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}

    # 初始化

    lis = [{"name": "Taobao", "age": 100},
           {"name": "Runoob", "age": 7},
           {"name": "Google", "age": 100},
           {"name": "Wiki", "age": 200}]

    print('字典key_value按键(key)排序:')

    # sorted(key_value) 返回重新排序的列表
    for i in sorted(key_value):
        print((i, key_value[i]))

    print("按值(value)排序:")
    print(sorted(key_value.items(), key=lambda kv: (kv[1], kv[0])))

    # 通过 age 升序排序
    print("字典lis通过 age 升序排序: ")
    print(sorted(lis, key=lambda i: i['age']))

    print("\r")

    # 先按 age 排序，再按 name 排序
    print("字典lis通过 age 和 name 排序: ")
    print(sorted(lis, key=lambda i: (i['age'], i['name'])))

    print("\r")

    # 按 age 降序排序
    print("字典lis通过 age 降序排序: ")
    print(sorted(lis, key=lambda i: i['age'], reverse=True))


def main():
    # 调用函数
    dictionairy()


# 主函数


if __name__ == '__main__':
    main()
