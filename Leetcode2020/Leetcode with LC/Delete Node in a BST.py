# coding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    # 寻找该root右分支最小值的节点
    def successor(self, root):
        root = root.right
        while root.left is not None:
            root = root.left
        return root.val

    # 寻找该root左分支最大值的节点
    def predecessor(self, root):
        root = root.left
        while root.right is not None:
            root = root.right
        return root.val

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return None

        # 如果目标值比该root.val大，则要去右分支
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        # 如果目标值比该root.val小，则要去左分支
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        # 如果目标值==root.val，要执行delete操作，并做一些判断
        else:
            # 该节点是叶子节点
            if root.left == None and root.right == None:
                root = None
            # 如果该节点有右子树
            elif root.right != None:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # 如果没有右子树
            else:
                root.val = self.deleteNode(root)
                root.left = self.deleteNode(root.left, root.val)

        return root