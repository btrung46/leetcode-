class Solution(object):
    def searchMatrix(self, matrix, target):
        for row in matrix:
            if row[0] <= target <= row[len(row)-1]:
                left = 0
                right = len(row) -1
                while (left <= right):
                    mid = (left + right) / 2
                    if row[mid] == target:
                        return True
                    elif row[mid] > target:
                        right = mid -1
                    else:
                        left = mid + 1
                return False
        return False
                