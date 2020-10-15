# coding: utf-8

import copy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if head.val == val:
            head = head.next

        node = head

        while node.next != None:
            if node.next.val == val:
                node.next = node.next.next
                break
            else:
                node = node.next

        return head

l = [4,5,1,9]
head = ListNode(l[0])
node = head
for i in xrange(1, len(l)):
    tag = ListNode(l[i])
    node.next = tag
    node = node.next

s = Solution()
s.deleteNode(head, 9)