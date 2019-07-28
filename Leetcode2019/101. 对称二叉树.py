# coding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isMirror(leftRoot, rightRoot):
            if leftRoot == None and rightRoot == None:
                return True
            if leftRoot == None or rightRoot == None:
                return False
            if leftRoot.val != rightRoot.val:
                return False

            oneSide = isMirror(leftRoot.left, rightRoot.right)
            otherSide = isMirror(leftRoot.right, rightRoot.left)

            if oneSide == True and otherSide == True:
                return True
            else:
                return False

        return isMirror(root, root)