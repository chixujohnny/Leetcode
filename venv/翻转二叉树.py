# coding:utf-8

# Definition for a binary tree node.
class root(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: root
        :rtype: root
        """

        if root == None:
            return
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        return root