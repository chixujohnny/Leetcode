# coding: utf-8

# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
# 如果不存在，则返回  -1。

# input: haystack = "hello", needle = "ll"
# output: 2

class Solution(object):

    def check(self, haystack, needle, i):
        position = i
        j = 0
        while True:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return position
                if i == len(haystack):
                    return -1
            else:
                return -2

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                ret = self.check(haystack, needle, i)
                if ret == -1:
                    return -1
                if ret == -2:
                    continue
                else:
                    return ret

        return -1

s = Solution()
print( s.strStr('a', 'a') )