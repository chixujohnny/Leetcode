class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.res = []

        def helper(nums, path, start):
            self.res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                helper(nums, path, i + 1)
                path.pop()

        helper(nums, [], 0)

        return self.res


s = Solution()
print s.subsets([1,2,3])