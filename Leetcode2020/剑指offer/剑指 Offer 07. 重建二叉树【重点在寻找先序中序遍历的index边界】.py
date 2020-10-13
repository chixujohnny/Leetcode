# coding: utf-8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == [] and inorder == []:
            return None

        def helper(preorder, inorder):
            if preorder == []:
                return None

            root_val = preorder[0]
            root = TreeNode(root_val)

            inorder_root_index = inorder.index(root_val)
            preorder_left = preorder[1:inorder_root_index+1]
            preorder_right = preorder[inorder_root_index+1:]
            inorder_left = inorder[:inorder_root_index]
            inorder_right = inorder[inorder_root_index+1:]

            root.left = helper(preorder_left, inorder_left)
            root.right = helper(preorder_right, inorder_right)

            return root

        return helper(preorder, inorder)

s = Solution()
s.buildTree([3,9,20,15,7], [9,3,15,20,7])