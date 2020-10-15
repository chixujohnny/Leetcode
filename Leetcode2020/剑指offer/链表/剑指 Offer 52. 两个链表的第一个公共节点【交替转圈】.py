# coding: utf-8

# 题解：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/shuang-zhi-zhen-fa-lang-man-xiang-yu-by-ml-zimingm/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if headA == None or headB == None:
            return None

        node1 = headA
        node2 = headB
        flag1 = False
        flag2 = False
        while node1 != node2:

            node1 = node1.next
            if node1 == None:
                if flag1 == False:
                    node1 = headB
                    flag1 = True
                else:
                    return None

            node2 = node2.next
            if node2 == None:
                if flag2 == False:
                    node2 = headA
                    flag2 = True
                else:
                    return None

        return node1
