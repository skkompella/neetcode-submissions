class Solution:
    def search(self, nums: List[int], target: int, offset=0) -> int:
        idx = len(nums)//2
        # offset = idx
        if (idx >= 1):
            if (target < nums[idx]):
                return self.search(nums[:idx], target, offset)
            elif (target > nums[idx]):
                return self.search(nums[idx:], target, idx+offset)
        if (target == nums[idx]):
            return idx+offset
        else:
            return -1