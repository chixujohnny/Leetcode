# coding: utf-8

class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binarySearch(nums, left_idx, right_idx, target):

            if left_idx > right_idx or right_idx < left_idx:
                return

            if left_idx == right_idx:
                if nums[left_idx] == target:
                    return left_idx
                else:
                    return

            # 判断哪边有序
            mid_idx = (left_idx + right_idx)/2
            mid = nums[mid_idx]

            # 如果mid大于最左边的数，则左边是有序的；若mid小于最右边的数，则右边是有序的
            if mid == target:
                return mid_idx

            if mid >= nums[left_idx]:
                if left_idx != mid_idx:
                    ret = binarySearch(nums, left_idx, mid_idx, target)
                    if ret != None:
                        return ret
                    ret = binarySearch(nums, mid_idx +1, right_idx, target)
                    if ret != None:
                        return ret
                    return
                else:
                    ret = binarySearch(nums, mid_idx + 1, right_idx, target)
                    if ret != None:
                        return ret

            if mid <= nums[right_idx] and right_idx != mid_idx:
                if right_idx != mid_idx:
                    ret = binarySearch(nums, mid_idx +1, right_idx, target)
                    if ret != None:
                        return ret
                    ret = binarySearch(nums, left_idx, mid_idx, target)
                    if ret != None:
                        return ret
                    return
                else:
                    ret = binarySearch(nums, left_idx, mid_idx, target)
                    if ret != None:
                        return ret

        ret = binarySearch(nums, 0, len(nums) -1, target)
        if ret != None:
            return ret
        else:
            return -1




s = Solution()
print s.search([1,3], 1)
print s.search([1], 1)
print s.search([3,1], 1)
print s.search([2,4,5,6,7,0,1], 9)
print s.search([2,4,5,6,7,0,1], 0)