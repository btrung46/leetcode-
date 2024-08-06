class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        n = len(nums)
        left = 1
        for i in range(n):
            result.append(left)
            left = left*nums[i]
        right = 1
        for i in range(n-1,-1,-1):
            result[i] *= right
            right *= nums[i]
        return result
       