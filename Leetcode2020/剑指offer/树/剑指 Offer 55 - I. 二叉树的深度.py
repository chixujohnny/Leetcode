# coding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1

        def helper(node, depth):
            if node == None:
                depth -= 1
                return depth
            left_depth = helper(node.left, depth+1)
            right_depth = helper(node.right, depth+1)
            depth = max(left_depth, right_depth)
            return depth

        return helper(root, 1)


treeList = [3,9,20,None,None,15,7]
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
print s.maxDepth(root)