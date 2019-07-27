# coding: utf-8

# 先序遍历：根 -> 左 -> 右

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        def helper(root):
            if root == None:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)

        return res