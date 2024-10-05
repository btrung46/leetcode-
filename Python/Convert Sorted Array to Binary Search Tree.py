
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        def ans(nums,start,end):
            if start > end:
                return 
            mid = (start + end)//2
            root = TreeNode(nums[mid])
            root.left = ans(nums,start, mid-1)
            root.right = ans(nums,mid+1,end)
            return root
        return ans(nums, 0,len(nums)-1)
            


        

        