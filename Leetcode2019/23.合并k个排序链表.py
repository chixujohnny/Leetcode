# coding: utf-8

# 合并 k 个排序链表，返回合并后的排序链表。
# 此题可以将所有链表的元素扔进list再qsort成链表

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # delete all NULL ListNode
        # for i, item in enumerate(lists):
        #     if item == None:
        #         lists.pop(i)
        i = 0
        while i < len(lists):
            if lists[i] == None:
                lists.pop(i)
            else:
                i += 1

        if len(lists) == 0:
            return None

        items = []
        for item in lists:
            while item != None:
                items.append(item.val)
                item = item.next

        items.sort()
        head = ListNode(items[0])
        tag = head
        for i in range(1, len(items)):
            tag.next = ListNode(items[i])
            tag = tag.next

        return head


# create a few ListNode
l = [1,4,5]
head1 = ListNode(l[0])
tag = head1
for i in range(1, len(l)):
    tag.next = ListNode(l[i])
    tag = tag.next

l = [1,3,4]
head2 = ListNode(l[0])
tag = head2
for i in range(1, len(l)):
    tag.next = ListNode(l[i])
    tag = tag.next

l = [2,6]
head3 = ListNode(l[0])
tag = head3
for i in range(1, len(l)):
    tag.next = ListNode(l[i])
    tag = tag.next


s = Solution()
head = s.mergeKLists([None, None])

# print ListNode
while head != None:
    print(head.val)
    head = head.next