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

        # 做这道题之前别忘了二叉搜索树的特性！！！

        def helper(root, p, q):
            if p.val < root.val and q.val < root.val:
                return helper(root.left, p, q)
            elif p.val > root.val and q.val > root.val:
                return helper(root.right, p, q)
            else:
                return root  # p q 分别分布在左右孩子中

        return helper(root, p, q)