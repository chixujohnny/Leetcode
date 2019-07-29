# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        res = []

        def helper(root, route):
            if root == None:
                return
            route += str(root.val)
            if root.left == None and root.right == None:
                res.append(route)
                return
            helper(root.left, route)
            helper(root.right, route)

        helper(root, '')

        ret = 0
        for item in res:
            ret += int(item)

        return ret