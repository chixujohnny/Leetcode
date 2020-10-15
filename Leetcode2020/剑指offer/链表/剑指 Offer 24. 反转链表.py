# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        node = head.next

        i = 0
        while node != None:
            if i == 0:  # 如果是第一轮
                head.next = None
                nodeNext = node.next
                node.next = head
                head = node
                node = nodeNext
                i += 1
            else:
                nodeNext = node.next
                node.next = head
                head = node
                node = nodeNext

        return head

l = [1]
head = ListNode(l[0])
node = head
for i in xrange(1, len(l)):
    tag = ListNode(l[i])
    node.next = tag
    node = node.next

s = Solution()
s.reverseList(head)