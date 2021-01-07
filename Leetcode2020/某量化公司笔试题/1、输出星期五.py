# coding: utf-8

# 1、输入某一年，输出这一年每个月最后一个星期五是哪一天，输出格式"2020-10-23"

# input = '2020'

def function(input):

    input = int(input)

    # 判断该年份是不是闰年
    # 能被4整除而不能被100整除
    # 能被400整除
    def IsLeapYear(year):
        if (year%4==0 and year%100!=0) or year%400==0:
            return True
        else:
            return False

    # 先看看是不是闰年
    is_leap_year = IsLeapYear(input)

    # 基准位2020-01-01周三
    # 先计算输入年的第一天是星期几
    # 1、计算年份差
    year_diff = 2020 - input
    # 2、目标年与2020-01-01中间夹着多少个0229
    def HowManyLeapDay(input):

        leapDayNum = 0

        if input < 2020:
            for year in range(input, 2020):
                if year == 0:
                    continue
                if IsLeapYear(year) == True:
                    leapDayNum += 1
        else:
            for year in range(2020, input):
                if IsLeapYear(year) == True:
                    leapDayNum += 1

        return leapDayNum

    leapDayNum = HowManyLeapDay(input)

    # 3、目标年份的第一天是星期几
    firstDayIndexDiff = (365*abs(input-2020) + leapDayNum) % 7
    if input < 2020:
        i = 3
        while firstDayIndexDiff > 0:
            i -= 1
            if i == 0:
                i = 7
            firstDayIndexDiff -= 1
    else:
        i = 3
        while firstDayIndexDiff > 0:
            i += 1
            if i == 8:
                i = 1
            firstDayIndexDiff -= 1

    # 这一年第一天是星期几
    firstDayoftheYear = i

    # 4、开始算每个月的最后一个星期五，暴力遍历吧
    res = []
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year == True:
        month = [31,29,31,30,31,30,31,31,30,31,30,31]
    today = firstDayoftheYear
    lastFridayDay = 0

    for m, days in enumerate(month):
        for d in range(days):
            if today == 5:
                lastFridayDay = d+1
            today += 1
            if today == 8:
                today = 1

        if m >= 9:
            if input > 0:
                res.append(str(input) + '-' + str(m + 1) + '-' + str(lastFridayDay))
            else:
                res.append(str(input)[1:] + '-' + str(m + 1) + '-' + str(lastFridayDay))
        else:
            if input > 0:
                res.append(str(input) + '-0' + str(m + 1) + '-' + str(lastFridayDay))
            else:
                res.append(str(input)[1:] + '-0' + str(m + 1) + '-' + str(lastFridayDay))

    return res


print function(-100)