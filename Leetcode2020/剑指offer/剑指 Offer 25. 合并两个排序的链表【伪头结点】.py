# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #   l1      l2
        #  [5, 6]  [1, 2, 4]
        #
        #  先看l1和l2谁更小，l2更小
        #  再看l1和l2.next谁更小

        #  边界条件
        if l1 == None and l2 == None:
            return None

        #  伪头结点
        dum = ListNode(-1)
        cur = dum

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = l2
                cur = cur.next
                l2 = l2.next

        if l1 != None and l2 == None:
            cur.next = l1
        else:
            cur.next = l2

        return dum.next



l1 = [5]
l1_head = ListNode(l1[0])
node = l1_head
for i in xrange(1, len(l1)):
    tag = ListNode(l1[i])
    node.next = tag
    node = node.next

l2 = [1,2,3]
l2_head = ListNode(l2[0])
node = l2_head
for i in xrange(1, len(l2)):
    tag = ListNode(l2[i])
    node.next = tag
    node = node.next

s = Solution()
head = s.mergeTwoLists(l1_head, l2_head)
while head != None:
    print head.val
    head = head.next