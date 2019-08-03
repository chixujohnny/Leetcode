"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        def helper(root):
            if root == None:
                return

            if root.left != None:
                root.left.next = root.right

            if root.next != None and root.right != None:
                root.right.next = root.next.left

            helper(root.left)
            helper(root.right)

            return root

        return helper(root)