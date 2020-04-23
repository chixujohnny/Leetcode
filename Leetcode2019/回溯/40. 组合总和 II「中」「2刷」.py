class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []

        def helper(candidates, target, path, total, start):

            if target == total and path not in res:
                res.append(path[:])

            for i in range(start, len(candidates)):

                if total + candidates[i] <= target:
                    path.append(candidates[i])
                    helper(candidates, target, sorted(path), total + candidates[i], i + 1)
                    path.pop()

        helper(candidates, target, [], 0, 0)

        return res


s = Solution()
s.combinationSum2([10,1,2,7,6,1,5], 8)



class Solution(object):

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        self.res = []

        def helper(candidates, target, path, start):
            if sum(path) == target and path not in self.res:
                self.res.append(path[:])
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                if sum(path) <= target:
                    helper(candidates, target, sorted(path), i+1)
                path.pop()

        helper(candidates, target, [], 0)

        return self.res








































