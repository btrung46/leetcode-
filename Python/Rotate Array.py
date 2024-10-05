class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0,k):
            a = nums.pop()
            nums.insert(0,a)