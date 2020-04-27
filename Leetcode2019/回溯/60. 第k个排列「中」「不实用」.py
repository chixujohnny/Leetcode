# coding: utf-8

# 题解：https://leetcode-cn.com/problems/permutation-sequence/solution/di-k-ge-pai-lie-by-leetcode/

# 要用到康托展开，感觉不是很实用，只写出来了回溯法，但是超时了。这道题不推荐二刷/复习，不够通用。

class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        res = []

        n_list = []
        for i in range(n):
            n_list.append(i+1)

        def helper(n_list, path):
            if len(res) == k:
                return

            if n_list == []:
                res.append(path[:])

            for i in range(len(n_list)):
                path.append(n_list[i])
                helper(n_list[:i]+n_list[i+1:], path)
                path.pop()


        helper(n_list, [])

        ret = ''
        for item in res[-1]:
            ret += str(item)

        return ret


s = Solution()
print s.getPermutation(9, 155915)