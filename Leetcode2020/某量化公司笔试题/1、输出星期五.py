# coding: utf-8

# 1、输入某一年，输出这一年每个月最后一个星期五是哪一天，输出格式"2020-10-23"

# input = '2020'

def function(input):

    input = int(input)

    # 判断该年份是不是闰年
    # 能被4整除而不能被100整除
    # 能被400整除
    def IsLeapYear(input):
        if (input%4==0 and input%100!=0) or input%400==0:
            return True
        else:
            return False

    # 先看看是不是闰年
    is_leap_year = IsLeapYear(input)

    # 基准位2020-01-01周三
    # 先计算输入年的第一天是星期几
    year_diff = abs(2020-input)