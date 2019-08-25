# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if head == None:
            return head
        if m == n:
            return head

        array = []
        node = head
        for i in range(m - 1):
            node = node.next
        node_tag = node

        for i in range(n - m + 1):
            array.append(node_tag.val)
            node_tag = node_tag.next
        array.reverse()

        for i in range(n - m + 1):
            node.val = array[i]
            node = node.next

        return head