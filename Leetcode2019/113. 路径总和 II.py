# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        res = []

        def helper(root, sum, route):
            if root == None:
                return

            if root.left == None and root.right == None and sum - root.val == 0:
                route.append(root.val)
                res.append(route)

            helper(root.left, sum - root.val, route + [root.val])
            helper(root.right, sum - root.val, route + [root.val])

        helper(root, sum, [])

        return res