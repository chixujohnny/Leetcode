# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        hashTable = {head.val: 0}
        pre = head
        node = head.next

        while node != None:
            if hashTable.has_key(node.val) == False:
                hashTable[node.val] = 0
                node = node.next
                pre = pre.next
            else:
                pre.next = node.next
                node = node.next

        return head