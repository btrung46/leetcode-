class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        for s in range(len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum < target:
                i += 1
            if sum > target:
                j -= 1
            if sum == target:
                return [i+1,j+1]
                


        