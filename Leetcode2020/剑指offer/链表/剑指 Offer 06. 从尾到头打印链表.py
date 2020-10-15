# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """

        res = []
        while head != None:
            print head.val
            res.append(head.val)
            head = head.next

        res.reverse()
        return res
