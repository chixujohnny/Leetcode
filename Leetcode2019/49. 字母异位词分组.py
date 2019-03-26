# coding: utf-8

# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# 我的思路：遍历input的每个单词时，做sort()再丢到相应的分组，每个分组都是dict，最后再将dict变成list作return

class Solution(object):

    def groupAnagrams(self, strs):

        if len(strs) == 0:
            return []

        d = {}
        for item in strs:
            item_sorted = ''.join(sorted(item))
            if d.has_key(item_sorted) == False:
                d[item_sorted] = [item]
            else:
                d[item_sorted].append(item)

        return d.values()

s = Solution()
print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])