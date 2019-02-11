# coding: utf-8

import copy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        if head.next == None and n == 1:
            return None
        if head.next == None and n == 0:
            return head

        left_node = head
        right_node = head

        # 让右节点在左节点右边n个位置
        for i in range(n):
            right_node = right_node.next
            if right_node == None:
                return head.next
        while True:
            if right_node.next == None:
                left_node.next = left_node.next.next
                break
            else:
                left_node = left_node.next
                right_node = right_node.next

        return head


# create a ListNode
l = [1,2]
head = ListNode(l[0])
tag = head
for i in range(1, len(l)):
    tag.next = ListNode(l[i])
    tag = tag.next


s = Solution()
head = s.removeNthFromEnd(head, 2)
while True:
    print( head.val )
    if head.next != None:
        head = head.next
    else:
        break