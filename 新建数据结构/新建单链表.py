# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

l = [4,5,1,9]
head = ListNode(l[0])
node = head
for i in xrange(1, len(l)):
    tag = ListNode(l[i])
    node.next = tag
    node = node.next