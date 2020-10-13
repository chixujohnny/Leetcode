# coding: utf-8

class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s == '':
            return []

        res = []
        def helper(s, path):
            if s == '':
                if path not in res:
                    res.append(path[:])
                    return

            for i in range(len(s)):
                path += s[i]
                helper(s[:i]+s[i+1:], path)
                path = path[:-1]

        helper(s, '')
        return res


ss = 'abc'

s = Solution()
print s.permutation(ss)