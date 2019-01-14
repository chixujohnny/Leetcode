# coding: utf-8

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        N_FLAG = ''
        num = ''
        str = str.lstrip(' ') # 去除开头的空格

        if str == "":
            return 0

        for i, item in enumerate(str):
            if item == '-' or item == '+':
                if N_FLAG == '' and num == '':
                    N_FLAG = item
                else:
                    return 0
            elif (ord(item) < 48 or ord(item) > 57) and item != '-':
                # 当前没有数存进去
                if num == '': return 0
                # 当前已经有数存进去了
                else: break
            elif ord(item) >= 48 and ord(item) <= 57:  # ascii码阿拉伯数字范围
                num += item

        # 如果只有负号
        if N_FLAG == '-' and num == '':
            return 0
        # 如果有正号
        if N_FLAG == '+' and num == '':
            return 0
        # str转int
        num = N_FLAG + num
        if num == '+0' or num == '-0':
            return 0
        num = int(num.replace('+',''))
        if num > INT_MAX: return INT_MAX
        elif num < INT_MIN: return INT_MIN
        else: return num

s = Solution()
print(s.myAtoi("-5-"))