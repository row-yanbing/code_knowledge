#!/usr/bin/python3
# -*- coding:UTF-8 -*-
import datetime


def format_date():
    """
    格式化日期
    :return:
    """
    date_f = '%d/%m/%Y'
    # 当前日期
    print(datetime.date.today().strftime(date_f))
    # 指定日期
    birthday = datetime.date(1992, 3, 14)
    print(birthday.strftime(date_f))
    # 指定日期 + days
    birthday_next_day = birthday + datetime.timedelta(days=1)
    print(birthday_next_day.strftime(date_f))
    # 修改指定日期的年份
    first_birthday = birthday.replace(year=birthday.year + 1)
    print(first_birthday.strftime(date_f))


if __name__ == '__main__':
    format_date()
