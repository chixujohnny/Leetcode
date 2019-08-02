# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def helper(nums):
            if nums == []:
                return

            mid_index = len(nums) / 2
            root = TreeNode(nums[mid_index])  # 取数组中最中间那个数最为根节点

            root.left = helper(nums[:mid_index])
            root.right = helper(nums[mid_index + 1:])

            return root

        return helper(nums)