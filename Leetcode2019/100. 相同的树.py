# coding: utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        res_p = []
        res_q = []

        def helper(node, res):
            if node == None:
                return

            res.append(node.val)

            if node.left == None:
                res.append(None)
            else:
                helper(node.left, res)

            if node.right == None:
                res.append(None)
            else:
                helper(node.right, res)

            return res

        res_p = helper(p, res_p)
        res_q = helper(q, res_q)

        if res_p == res_q:
            return True
        else:
            return False
