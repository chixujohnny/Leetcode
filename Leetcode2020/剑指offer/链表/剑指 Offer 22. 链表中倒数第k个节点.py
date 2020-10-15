# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == None:
            return None

        firstNode = head
        for i in range(k-1):
            if firstNode.next == None:
                return None
            firstNode = firstNode.next

        preNode = head
        while firstNode.next != None:
            firstNode = firstNode.next
            preNode = preNode.next

        return preNode


l = [1,2,3,4,5]
head = ListNode(l[0])
node = head
for i in xrange(1, len(l)):
    tag = ListNode(l[i])
    node.next = tag
    node = node.next

s = Solution()
preNode = s.getKthFromEnd(head, 2)
print(preNode.val)