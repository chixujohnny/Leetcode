# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 解法1:Hash-table比较简单就不写了

        # 解法2：Floyd算法
        #       第一阶段判断是否成环：设置一个快指针+慢指针，当快指针追上慢指针并相交时认为该链表有环形结构，该node标记为tag_node；若有遇上node.next==None则不成环
        #       第二阶段判断成环起点：head与f_node同时向前走，遇到的交点即为成环的起点，它们向前走的步数即为index

        if head == None:
            return -1

        # stage1
        if head.next == None and head.next.next == None:
            return -1

        index_node = head
        s_node = head.next
        f_node = head.next.next

        while s_node != f_node:
            if f_node.next != None and f_node.next.next != None:
                s_node = s_node.next
                f_node = f_node.next.next
            else:
                return -1
        tag_node = s_node

        # stage2
        i = 0
        while index_node != tag_node:
            index_node= index_node.next
            tag_node = tag_node.next
            i += 1
        return i


# 创建环形链表
nums = [3,2,0,-4]
pos = 1
head = ListNode(nums[0])
node = head
for i in range(1, len(nums)):
    node.next = ListNode(nums[i])
    node = node.next
    if i == pos:
        pre_node = node
node.next = pre_node

s = Solution()
print s.detectCycle(head)