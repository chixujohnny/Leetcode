# coding: utf-8

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            if n%2 == 0:
                return (nums2[n/2-1] + nums2[n/2])/float(2)
            else:
                return nums2[(n-1)/2]
        if n == 0:
            if m%2 == 0:
                return (nums1[m/2-1] + nums1[m/2])/float(2)
            else:
                return nums1[(m-1)/2]
        if (m+n)%2 == 1:
            i = 0
            j = 0
            tag = 0
            i_close_flag = 0
            j_close_flag = 0
            while True:
                if (nums1[i] <= nums2[j] or j_close_flag == 1) and i_close_flag == 0:
                    if tag == (m+n-1)/2:
                        return nums1[i]
                    tag += 1
                    i += 1
                    if i >= m:
                        i_close_flag = 1
                        i -= 1
                    continue
                if (nums1[i] > nums2[j] or i_close_flag == 1) and j_close_flag == 0:
                    if tag == (m+n-1)/2:
                        return nums2[j]
                    j += 1
                    tag += 1
                    if j >= n:
                        j_close_flag = 1
                        j -= 1

        else:
            i = 0
            j = 0
            tag = 0
            mid_l = 0
            i_close_flag = 0
            j_close_flag = 0
            while True:
                if i_close_flag == 0:
                    if nums1[i] <= nums2[j] or j_close_flag == 1:
                        if tag == (m+n)/2-1:
                            mid_l = nums1[i]
                        if tag == (m+n)/2:
                            return (mid_l+nums1[i])/float(2)
                        i += 1
                        tag += 1
                        if i >= m:
                            i_close_flag = 1
                            i -= 1
                        continue
                if  j_close_flag == 0:
                    if nums1[i] > nums2[j] or i_close_flag == 1:
                        if tag == (m+n)/2-1:
                            mid_l = nums2[j]
                        if tag == (m+n)/2:
                            return (mid_l+nums2[j])/float(2)
                        j += 1
                        tag += 1
                        if j >= n:
                            j_close_flag = 1
                            j -= 1


x = Solution()
print x.findMedianSortedArrays([3],[-2,-1])
print x.findMedianSortedArrays([1,2],[3,4])
print x.findMedianSortedArrays([1],[2,3])