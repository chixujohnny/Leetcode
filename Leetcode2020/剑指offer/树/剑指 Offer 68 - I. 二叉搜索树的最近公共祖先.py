# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
            if root == p or root == q:
                return root

            left = helper(root.left, p, q)
            right = helper(root.right, p, q)

            if left == None:
                return right
            if right == None:
                return left

            return root

        return helper(root, p, q)