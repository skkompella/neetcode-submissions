class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        mid = l // 2
        if l == 1:
            return nums[0]
        if l <= 2:
            return min(nums[0], nums[1])
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        if nums[mid+1] < nums[mid]:
            return nums[mid+1]
        return min(self.findMin(nums[:mid]), self.findMin(nums[mid:]))