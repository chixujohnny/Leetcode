# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None

        # 统计两链表长度
        tagA = headA
        len_A = 0
        while tagA != None:
            len_A += 1
            tagA = tagA.next

        tagB = headB
        len_B = 0
        while tagB != None:
            len_B += 1
            tagB = tagB.next

        if len_A == len_B:
            # 两链表一起向前走，直到相交为止
            while headA != headB:
                headA = headA.next
                headB = headB.next
            return headA

        else:
            # 减掉比较长的链表长出来的几个节点
            for i in range(abs(len_B-len_A)):
                if len_B > len_A:
                    headB = headB.next
                if len_A > len_B:
                    headA = headA.next

            # 两链表一起向前走，直到相交为止
            while headA != headB:
                headA = headA.next
                headB = headB.next

            return headA