# Now, does this still work even if the duplicate numbers aren't next to each other in the array? 
# The answer is yes, it will, because XOR is both communative and associative, 
# meaning that a XOR b = b XOR a, and (a XOR b) XOR c = a XOR (b XOR c). 
# This means that no matter what order the numbers are in, 
# the numbers that appear twice will always cancel out to 0 and we will be left with the single number.

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         answer = 0
#         for num in nums:
#             answer ^= num
#         return answer
 
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            if dic[i] == 1:
                return i

        