# coding: utf-8

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
        if root == None:
            return True

        def helper(root):
            if root == None:
                return
            return max(root.left, root.right) + 1

        if abs(helper(root.left)-helper(root.right)) <= 1 and self.isBalanced(root.left) == True and self.isBalanced(root.right) == True:
            return True
        else:
            return False