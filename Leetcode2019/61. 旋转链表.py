# coding: utf-8

import copy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def rotateRight(self, head, k):

        if k == 0:
            return head
        if head == None:
            return head

        # 先看一下这个链表有多长
        node = head
        length = 0
        while node != None:
            length += 1
            node = node.next

        # 取k对length的余数
        k = k % length

        # 设置并移动l、r指针
        r = head
        for i in range(k):
            r = r.next
        l = head
        while r.next != None:
            r = r.next
            l = l.next

        r.next = head
        head = l.next
        l.next = None

        return head

# 构造单链表
item = [0,1,2]
head = ListNode(item[0])
node = head
for i in range(1, len(item)):
    node.next = ListNode(item[i])
    node = node.next

# print链表
node = head
while node != None:
    print node.val
    node = node.next

s = Solution()
ret = s.rotateRight(head, k=4)
print ret.val