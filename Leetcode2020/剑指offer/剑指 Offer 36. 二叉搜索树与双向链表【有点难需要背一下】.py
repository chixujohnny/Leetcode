# coding: utf-8

# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root == None:
            return

        self.pre = None

        def helper(cur):
            if cur == None:
                return
            helper(cur.left)  # 递归左子树
            if self.pre != None:
                self.pre.right = cur
                cur.left = self.pre
            else: # 记录头结点
                self.head = cur
            self.pre = cur
            helper(cur.right) # 递归右子树

        helper(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head