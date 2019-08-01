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

        self.res = None

        def helper(root, p, q):
            if root == None:
                return False

            left = helper(root.left, p, q)
            right = helper(root.right, p, q)

            if left == True or right == True:
                if root == p or root == q:
                    self.res = root
                elif left == True and right == True:
                    self.res = root
                else:
                    return True
            if root == p or root == q:
                return True
            else:
                return False

        helper(root, p, q)

        return self.res