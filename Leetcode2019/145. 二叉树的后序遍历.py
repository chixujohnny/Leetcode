# coding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        def helper(root):
            if root == None:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)

        helper(root)

        return res