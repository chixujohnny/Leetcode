# coding: utf-8

import copy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head

        l_node = copy.copy(head)
        r_node = head.next
        # only have 2 ListNode
        if r_node.next == None:
            l_node.next = None
            r_node.next = l_node
            return r_node

        # more than 2 ListNode
        first_flag = 1
        while r_node != None:
            # replace
            if first_flag == 1:
                l_node.next = r_node.next
                r_node.next = l_node
                head = r_node
                tag = l_node
                if l_node.next == None or l_node.next.next == None:
                    break
                else:
                    r_node = l_node.next.next
                    l_node = l_node.next
                    first_flag = 0
            l_node.next = r_node.next
            tag.next = r_node
            r_node.next = l_node
            if l_node.next == None or l_node.next.next == None:
                break
            else:
                tag = l_node
                r_node = l_node.next.next
                l_node = l_node.next

        return head

# create a ListNode
l = [1,2]
head = ListNode(l[0])
tag = head
for i in range(1, len(l)):
    tag.next = ListNode(l[i])
    tag = tag.next

s = Solution()
head = s.swapPairs(head)

while head != None:
    print( head.val )
    head = head.next