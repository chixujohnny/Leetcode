# coding: utf-8

# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

# 输入: s = "paper", t = "title"
# 输出: true

# 输入: s = "ab", t = "aa"
# 输出: false

class Solution(object):

    def isIsomorphic(self, s, t):

        if len(s) == 0:
            return True

        dict_l = {}
        dict_r = {}
        for i in range(len(s)):
            if dict_l.has_key(s[i]) == False and dict_r.has_key(t[i]) == False:
                dict_l[s[i]] = t[i]
                dict_r[t[i]] = s[i]
            if dict_l.has_key(s[i]) == False and dict_r.has_key(t[i]) == True:
                return False
            if t[i] != dict_l[s[i]]:
                return False
        return True

s = Solution()
print s.isIsomorphic('ab','cc')
print s.isIsomorphic('foo','bar')
print s.isIsomorphic('agg','add')
print s.isIsomorphic('paper','title')