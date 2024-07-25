class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i,num in enumerate(nums):
            ans = target- num
            if ans in dic:
                return (dic[ans],i)
            dic[num]= i
        