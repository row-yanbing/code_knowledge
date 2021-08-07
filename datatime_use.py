# -*- codiyng: UTF-8 -*-
# Filename : datatime_use
# author by : yanbing

# 引入 datetime 模块
import datetime
import time

"""
计算3天前并转换为指定格式
"""
# 实例一
# 先获得时间数组格式的日期
threeDayAgo = (datetime.datetime.now() - datetime.timedelta(days=3))
# 转换为时间戳
timeStamp = int(time.mktime(threeDayAgo.timetuple()))
# 转换为其他字符串格式
otherStyleTime = threeDayAgo.strftime("%Y-%m-%d %H:%M:%S")
print(otherStyleTime)

# 实例二
# 给定时间戳
timeStamp1 = 1557502800
dateArray = datetime.datetime.utcfromtimestamp(timeStamp1)
threeDayAgo = dateArray - datetime.timedelta(days=3)
print(threeDayAgo)

"""
获取昨天的日期
"""
# datetime 模块来获取昨天的日期

def get_yesterday():
    yesterday = datetime.date.today() + datetime.timedelta(-1)
    return yesterday

# 输出
print(get_yesterday())
