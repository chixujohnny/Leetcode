# coding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if A == None or B == None:
            return False

        def helper(A, B):
            if B == None:
                return True
            if A == None or A.val != B.val:
                return False

            left = helper(A.left, B.left)
            right = helper(A.right, B.right)
            return left and right

        if helper(A, B) == True or self.isSubStructure(A.left, B) == True or self.isSubStructure(A.right, B) == True:
            return True
        else:
            return False


AList = [1,0,1,-4,-3]
BList = [1,-4]

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

A = CreateBineryTree(None, AList, 0)
B = CreateBineryTree(None, BList, 0)


s = Solution()
print s.isSubStructure(A, B)