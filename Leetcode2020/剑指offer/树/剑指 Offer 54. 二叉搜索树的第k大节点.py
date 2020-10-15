# coding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return None

        res = []
        def helper(root):
            if root == None:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res[-k]


treeList = [5,3,6,2,4,None,None,1]

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
s.kthLargest(root, k=3)