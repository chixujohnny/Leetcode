# coding: utf-8

# class Solution(object):
#     def permuteUnique(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#
#         res = []
#
#         def helper(nums, path):
#
#             if nums == [] and path not in res:
#                 res.append(path[:])
#                 return
#
#             for i in range(len(nums)):
#                 path.append(nums[i])
#                 helper(nums[:i] + nums[i + 1:], path)
#                 path.pop()
#
#         helper(nums, [])
#
#         return res
#
#
# s = Solution()
# print s.permuteUnique([1,1,2])





class Solution(object):

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def helper(nums, path):
            if nums == [] and path not in res:
                return res.append(path[:])

            for i in range(len(nums)):
                path.append(nums[i])
                helper(nums[:i]+nums[i+1:], path)
                path.pop()

            return res

        return helper(nums, [])


s = Solution()
print s.permuteUnique([1,1,2])

























