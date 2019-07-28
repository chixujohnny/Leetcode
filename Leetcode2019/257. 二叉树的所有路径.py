# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        res = []

        def helper(root, route, res):
            if root == None:
                return

            # 写当前路径
            if route == '':
                route = route + str(root.val)
            else:
                route = route + "->" + str(root.val)

            if root.left == None and root.right == None:
                res.append(route)  # 碰到了叶子节点走到尽头，把路径写到res中

            helper(root.left, route, res)
            helper(root.right, route, res)

        helper(root, '', res)

        return res
