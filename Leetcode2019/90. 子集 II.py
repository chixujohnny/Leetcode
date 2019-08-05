class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def helper(nums, path, start):
            if path not in res:
                res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                helper(nums, sorted(path), i + 1)
                path.pop()

        helper(nums, [], 0)
        return res

s = Solution()
# print s.subsetsWithDup([4,4,4,1,4])
print s.subsetsWithDup([1,2,2])