# coding: utf-8

# 给定一个正整数，返回它在 Excel 表中相对应的列名称。

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...

class Solution(object):

    def convertToTitle(self, n):

        ret = ''
        # n = n - 1
        while n != 0:
            ret += chr((n-1)%26 + 65)
            n = (n-1)/26

        return ret[::-1]

s = Solution()
print s.convertToTitle(701)
print s.convertToTitle(26)
print s.convertToTitle(52)