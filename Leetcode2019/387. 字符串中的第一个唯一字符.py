# coding: utf-8

# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# s = "leetcode"
# 返回 0.

# s = "loveleetcode",
# 返回 2.

class Solution(object):

    def firstUniqChar(self, s):


        if len(s) == 0:
            return -1

        # 我的答案时间复杂度O(2n)
        s_dict = {}
        for item in s:
            if s_dict.has_key(item) == False:
                s_dict[item] = 1
            else:
                s_dict[item] += 1
        for i, item in enumerate(s):
            if s_dict[item] == 1:
                return i
        return -1

        # 最优解时间复杂度O(n)
        # 直接把26个字母列出来，出现了就pop掉

s = Solution()
print s.firstUniqChar('ccddjjddjj')
print s.firstUniqChar('leetcode')
print s.firstUniqChar('loveleetcode')