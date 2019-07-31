# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        parent_part = 'left'

        def helper(root, level):
            if root == None:
                return

            if len(res) == level:
                res.append([])

            if level % 2 == 0:
                res[level] = [root.val] + res[level]
            else:
                res[level].append(root.val)

            helper(root.right, level + 1)
            helper(root.left, level + 1)

        helper(root, 0)

        return res