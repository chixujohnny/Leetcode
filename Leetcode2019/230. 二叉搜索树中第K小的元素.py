# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.res = []

        def helper(root):
            if root == None:
                return []

            left = helper(root.left)
            mid = [root.val]
            right = helper(root.right)

            return left + mid + right

        return helper(root)[k - 1]