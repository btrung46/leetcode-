class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        i = 0
        dem = 0 
        while(j < m+n):
            if nums1[j] == 0:
                nums1[j] = nums2[i]
                i+=1
            if i == len(nums2):
                break
            j+=1
        nums1.sort()