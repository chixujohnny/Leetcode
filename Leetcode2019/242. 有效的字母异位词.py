# coding: utf-8

# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

# 输入: s = "anagram", t = "nagaram"
# 输出: true

# 输入: s = "rat", t = "car"
# 输出: false

class Solution(object):

    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        s_dict = {}
        for item in s:
            if s_dict.has_key(item) == False:
                s_dict[item] = 1
            else:
                s_dict[item] += 1

        for i in range(len(t)):
            if s_dict.has_key(t[i]) == True:
                if s_dict[t[i]] > 0:
                    s_dict[t[i]] -= 1
                else:
                    return False
            else:
                return False
        return True

s = Solution()
print s.isAnagram("anagtam","nbgbram")
print s.isAnagram('rat','car')
print s.isAnagram('anagram','nagaram')