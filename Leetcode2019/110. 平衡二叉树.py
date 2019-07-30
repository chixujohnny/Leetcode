# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        self.res = True

        def helper(root):
            if root == None:
                return 0

            left_depth = helper(root.left) + 1
            right_depth = helper(root.right) + 1

            if abs(left_depth - right_depth) <= 1:
                return max(left_depth, right_depth)
            else:
                self.res = False
                return max(left_depth, right_depth)

        helper(root)

        return self.res