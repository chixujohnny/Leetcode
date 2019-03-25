# coding: utf-8

# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
# 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。

# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true

# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false

class Solution(object):

    def wordPattern(self, pattern, str):

        str = str.split(' ')

        if len(pattern) != len(str):
            return False
        if len(pattern) == 0:
            return True

        dict_l = {}
        dict_r = {}
        for i in range(len(pattern)):
            if dict_l.has_key(pattern[i]) == False and dict_r.has_key(str[i]) == False:
                dict_l[pattern[i]] = str[i]
                dict_r[str[i]] = pattern[i]
            if dict_l.has_key(pattern[i]) == False and dict_r.has_key(str[i]) == True:
                return False
            if str[i] != dict_l[pattern[i]]:
                return False
        return True

s = Solution()
print s.wordPattern('abba','dog cat cat dog')
print s.wordPattern('ab','cat cat')