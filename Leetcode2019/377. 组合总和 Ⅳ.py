class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        res = []

        def helper(nums, target, total, path):

            if total == target:
                res.append(path[:])
                print path
                # return

            for i in range(len(nums)):

                if total <= target:
                    helper(nums, target, total + nums[i], path + [nums[i]])

        helper(nums, target, 0, [])

        return len(res)

s = Solution()
print s.combinationSum4([4,2,1], 32)