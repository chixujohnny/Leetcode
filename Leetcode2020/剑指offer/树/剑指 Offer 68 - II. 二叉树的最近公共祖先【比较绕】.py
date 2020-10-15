# coding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def helper(root, p, q):
            if root == None:
                return None
            if root.val == p or root.val == q:
                return root.val

            left = helper(root.left, p, q)
            right = helper(root.right, p, q)

            if left == None:
                return right
            if right == None:
                return left

            return root.val


        return helper(root, p, q)

treeList = [3,5,1]
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
print s.lowestCommonAncestor(root, 5, 1)