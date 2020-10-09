# coding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None

        def helper(root):
            if root == None:
                return
            tag = root.right
            root.right = root.left
            root.left = tag
            helper(root.left)
            helper(root.right)
            return root

        return helper(root)

treeList = [4,2,7,1,3,6,9]
def CreateBineryTree(root, treeList, i):

    if i < len(treeList):
        if treeList[i] == None:
            return None
        else:
            root = TreeNode(treeList[i])
            root.left  = CreateBineryTree(root.left,  treeList, 2*i+1)
            root.right = CreateBineryTree(root.right, treeList, 2*i+2)
            return root
    return root
root = CreateBineryTree(None, treeList, 0)

s = Solution()
s.mirrorTree(root)