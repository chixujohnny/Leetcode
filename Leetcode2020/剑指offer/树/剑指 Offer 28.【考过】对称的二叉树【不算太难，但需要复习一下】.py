# coding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        def helper(L, R):
            if L == None and R == None:
                return True
            if L == None or R == None or L.val != R.val:
                return False

            left = helper(L.left, R.right)
            right = helper(L.right, R.left)

            if left == True and right == True:
                return True
            else:
                return False

        return helper(root.left, root.right)



treeList = [1,2,2,3,4,4,3]

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
print s.isSymmetric(root)