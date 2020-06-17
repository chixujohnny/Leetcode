# coding: utf-8

import copy

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []

        #  判断是否为回文串
        #  回文串定义：该string正着读、反着读是一样的
        def isPalString(path):

            if len(path) == 1:
                return True
            if len(path) == 0:
                return False

            readAsc = ''
            for item in path:
                readAsc += item

            readDesc = ''
            for item in reversed(path):
                readDesc += item

            if readAsc == readDesc:
                return True
            else:
                return False

        def helper(s, path):

            if isPalString(path) == True:
                res.append(path[:])


            for i in range(1, len(s)):
                path = path + s[:i]
                helper(s[i:], path)
                path = path[:-1]

        helper(s, '')

        return res


s = Solution()
print s.partition('aab')