# coding: utf-8

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return head
        cur = head
        while cur:
            new_node = Node(cur.val, None, None)  # 克隆新结点
            new_node.next = cur.next
            cur.next = new_node  # 克隆新结点在cur 后面
            cur = new_node.next  # 移动到下一个要克隆的点
        cur = head

        while cur:  # 链接random
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur_old_list = head  # 将两个链表分开
        cur_new_list = head.next
        new_head = head.next
        while cur_old_list:
            cur_old_list.next = cur_old_list.next.next
            cur_new_list.next = cur_new_list.next.next if cur_new_list.next else None
            cur_old_list = cur_old_list.next
            cur_new_list = cur_new_list.next
        return new_head