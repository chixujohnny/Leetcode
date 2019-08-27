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

        l = []
        node = head
        while node != None:
            l.append(node.val)
            node = node.next

        d = {}
        for item in l:
            if d.has_key(item) == False:
                d[item] = 1
            else:
                d[item] += 1

        h = None
        for item in l:
            if d[item] == 1:
                if h == None:
                    h = ListNode(item)
                    node = h
                else:
                    new = ListNode(item)
                    node.next = new
                    node = new

        return h