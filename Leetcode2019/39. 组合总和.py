# coding: utf-8

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        def helper(candidates, target, path):

            if sum(path) == target and path not in res:
                res.append(path[:])

            for i in range(len(candidates)):
                path.append(candidates[i])
                if sum(path) <= target:
                    helper(candidates, target, sorted(path))
                path.pop()

        helper(candidates, target, [])

        return res



s = Solution()
print s.combinationSum([2,3,6,7], 7)