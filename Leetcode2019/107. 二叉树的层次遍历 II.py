# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []

        def helper(root, level):
            if root == None:
                return

            if len(res) == level:
                res.append([])

            res[level].append(root.val)

            helper(root.left, level + 1)
            helper(root.right, level + 1)

        helper(root, 0)

        return reversed(res)