class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        dem = 1
        ans = []
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                dem += 1 
            elif nums[i+1] - nums[i] == 0:
                ans.append(dem)
                continue
            else:
                dem = 1
            ans.append(dem)
        return max(ans)