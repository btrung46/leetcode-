class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums) - 1 
        left = 0
        right = n
        while(left <= right):
            mid = (left + right)/2          
            if mid < n and nums[mid] <= nums[mid+1]:
                left = mid+1
            elif mid > 0 and nums[mid] <= nums[mid-1]:
                right = mid-1
            else: 
                return mid
        return 0