# coding: utf-8

import copy

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        res = []
        path = []

        def helper(root, tar):
            if root == None:
                return
            path.append(root.val)
            tar = tar - root.val
            if root.left == None and root.right == None and tar == 0:
                res.append(list(path))
            helper(root.left, tar)
            helper(root.right, tar)
            path.pop()

        helper(root, sum)
        return res



treeList = [5,4,8,11,None,13,4,7,2,None,None,5,1]

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
print s.pathSum(root, 22)