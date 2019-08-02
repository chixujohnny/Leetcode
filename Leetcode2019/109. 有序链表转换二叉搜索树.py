# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def findMidNode(head):

            mid_node_left = head
            node_slow = head
            node_fast = head

            while node_fast != None and node_fast.next != None:
                mid_node_left = node_slow
                node_slow = node_slow.next
                node_fast = node_fast.next.next

            return mid_node_left, node_slow

        def helper(head):

            if head == None:
                return
            if head.next == None:
                return TreeNode(head.val)

            mid_node_left, mid_node = findMidNode(head)
            root = TreeNode(mid_node.val)

            left_head = head
            right_head = mid_node.next
            mid_node_left.next = None

            root.left = helper(left_head)
            root.right = helper(right_head)

            return root

        return helper(head)


input = [1,2,3]
head = ListNode(input[0])
node = head
for item in input[1:]:
    node.next = ListNode(item)
    node = node.next

s = Solution()
s.sortedListToBST(head)