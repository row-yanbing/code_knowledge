# -*- coding: UTF-8 -*-
# Filename : calendar_use
# author by : yanbing

# 引入日历模块
import calendar

# 输入指定年月
yy = int(input("输入年份: "))
mm = int(input("输入月份: "))
#计算2016年9月份的第一天是星期几（0-6），这个月的天数
monthRange = calendar.monthrange(yy,mm)

# 显示日历
print(calendar.month(yy, mm))
#星期四，该月总共有 30 天
print(f'{yy}年的{mm}月的第一天是星期{monthRange[0]+1},该月共有{monthRange[1]}天')
