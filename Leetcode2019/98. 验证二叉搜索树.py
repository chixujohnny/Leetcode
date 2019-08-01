# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        self.res = True

        def helper(root, lower, upper):
            if root == None:
                return

            if root.val <= lower or root.val >= upper:
                self.res = False

            helper(root.left, lower, root.val)
            helper(root.right, root.val, upper)

        helper(root, float('-inf'), float('inf'))

        return self.res