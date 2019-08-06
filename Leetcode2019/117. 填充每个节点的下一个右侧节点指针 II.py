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

            if root.left != None and root.right != None:
                root.left.next = root.right

            if root.next != None:

                if root.right != None:
                    if root.next.left != None:
                        root.right.next = root.next.left
                    elif root.next.right != None:
                        root.right.next = root.next.right

                if root.left != None:
                    if root.next.left != None:
                        root.left.next = root.next.left
                    elif root.next.right != None:
                        root.left.next = root.next.right

            helper(root.left)
            helper(root.right)

            return root

        return helper(root)