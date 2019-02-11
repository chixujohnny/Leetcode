# coding: utf-8

import copy

# 此题很难

# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]

#   (此题搁置，暂时没有很好的解法)

class Solution(object):

    def recursive(self, candidates, target, i, pre=[], ret=[]):

        if i == len(candidates):
            return

        st = []
        while candidates[i] < target:
            target -= candidates[i]
            st.append(candidates[i])

        if target == 0:
            ret.append(pre + st)
        else:
            self.recursive(candidates, target, i+1, pre+st, ret)

        while st:
            target += st.pop()
            self.recursive(candidates, target, i+1, pre+st, ret)

    def combinationSum(self, candidates, target):

        ret = []
        self.recursive(candidates, target, 0, pre=[], ret=[])
        return ret

s = Solution()
s.combinationSum([2,3,6,7], 7)