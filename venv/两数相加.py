# coding: utf-8

# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
import copy



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

a = '243'
b = '564'

for i, item in enumerate(a):
    if i == 0:
        L1_head = ListNode(item)
        L = L1_head
    else:
        L.next = ListNode(item)
        L = L.next

for i, item in enumerate(b):
    if i == 0:
        L2_head = ListNode(item)
        L = L2_head
    else:
        L.next = ListNode(item)
        L = L.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = ''
        while l1 != None:
            a = str(l1.val) + a
            l1 = l1.next
        a = int(a)

        b = ''
        l = l2
        while l2 != None:
            b = str(l2.val) + b
            l2 = l2.next
        b = int(b)

        c = str(a+b)
        for i, item in enumerate(c[::-1]):
            if i == 0:
                l_head = ListNode(item)
                l = l_head

            else:
                l.next = ListNode(item)
                l = l.next

        return l_head

x = Solution()
l = x.addTwoNumbers(L1_head, L2_head)
while l != None:
    print(l.val)
    l = l.next