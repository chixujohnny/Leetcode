# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        while head != None and head.val == val:
            head = head.next

        if head == None:
            return None

        pre = head
        node = head.next

        while node != None:
            if node.val == val:
                pre.next = node.next
                node = node.next
            else:
                pre = pre.next
                node = node.next

        return head