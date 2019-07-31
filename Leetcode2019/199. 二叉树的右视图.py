# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []

        def helper(root, level):
            if root == None:
                return

            if len(res) == level:
                res.append([])

            res[level] = [root.val] + res[level]

            helper(root.right, level + 1)
            helper(root.left, level + 1)

        helper(root, 0)

        ret = []
        for l in res:
            ret.append(l[-1])

        return ret