class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        res = []
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def helper(nums, k, n, total, path, start):

            if total == n and len(path) == k:
                res.append(path[:])

            for i in range(start, len(nums)):
                if path == []:
                    helper(nums, k, n, total + nums[i], [nums[i]], i + 1)
                elif total <= n and len(path) <= k:
                    helper(nums, k, n, total + nums[i], path+[nums[i]], i + 1)

        helper(nums, k, n, 0, [], 0)

        return res


s = Solution()
print s.combinationSum3(3, 7)