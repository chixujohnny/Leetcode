# coding: utf-8

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        if pushed == [] and popped == []:
            return True

        i = 0
        stack = []
        for item in pushed:
            stack.append(item)
            while stack != [] and popped[0] == stack[-1]:
                popped.pop(0)
                stack.pop()

        if stack == []:
            return True
        else:
            return False


pushed = [1,2,3,4,5]
popped = [3,2,4,5,1]

s = Solution()
print s.validateStackSequences(pushed, popped)