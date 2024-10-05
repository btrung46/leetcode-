class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            if i > 0:
                if nums[i] == nums[i-1]:
                    continue
            while j<k:  
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j+=1
                elif total > 0:
                    k-=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
        return ans
        

