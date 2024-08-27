class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        dem = 0
        while(i < len(nums) and j <len(nums)):
            if nums[i] == nums[j]:
                dem += 1 
            else:
                dem = 0 
                i = j
            if dem > 1:
                dem -= 1
                del nums[j]
                j -= 1  
            j+=1
        return len(nums)

        