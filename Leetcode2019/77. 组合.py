# coding: utf-8

# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
# 示例:
# 输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

# 这个题目是典型的递归问题，即大规模问题可以转变成小规模的与原问题形式一样的子问题，诸如此类的问题还有“爬梯子”“斐波那契数列”等等，使用递归最主要是要明确这三点，递归的终止条件，递归终止时的处理办法，提取重复逻辑来减小问题规模。

import copy

class Solution(object):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """

    def combine(self, n, k):

#                           保存最终结果    存每次结果的临时list    s表示下一轮递归从哪个index开始往下捞数
        def recursive(n, k, ret=[],        pre=[],                s=1):
            if n == 0 and k == 0:
                return ret
            if k == 1:
                for i in range(s, n + 1):
                    pre.append(i)
                    ret.append(copy.copy(pre))
                    pre.pop()
                return ret
            for i in range(s, n - k + 2):
                pre.append(i)
                recursive(n, k - 1, ret, pre, i + 1)
                pre.pop()


    def combine2(self, n, k):   #  我写的第二种解法，看着好理解一些
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []

        def helper(n, k, path, start):
            if len(path) == k:
                res.append(path[:])

            for i in range(start, n):
                if len(path) <= k:
                    path.append(i + 1)
                    helper(n, k, path, i + 1)
                    path.pop()

        helper(n, k, [], 0)

        return res


        ret = []
        recursive(n, k, ret)

        return ret



s = Solution()
x = s.combine(4, 2)
print x