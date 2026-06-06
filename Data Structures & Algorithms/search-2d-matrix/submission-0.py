class Solution:
    def binarySearch(self, li, target):
        idx = len(li)//2
        if idx >= 1:
            if li[idx] < target:
                return self.binarySearch(li[idx:], target)
            elif li[idx] > target:
                return self.binarySearch(li[:idx], target)
        if li[idx] == target:
            return True
        else:
            return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        for i in range(M):
            if (self.binarySearch(matrix[i], target) == True):
                return True
        return False
