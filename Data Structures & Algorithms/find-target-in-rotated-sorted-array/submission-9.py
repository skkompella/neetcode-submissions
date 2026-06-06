class Solution:
    def search(self, nums: List[int], target: int, idx=-1) -> int:
        l = 0
        r = len(nums) - 1
        m = (l+r)//2
        if nums[m] == target:
            return m
        cnt = 0
        while l < r:
            mid = (l+r)//2
            if r-l <= 1:
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r
                return -1
            if nums[mid] < nums[r]: # means right half is sorted
                if target >= nums[mid] and target <= nums[r]: # in right half
                    l = mid
                else: # in left half
                    r = mid
            if nums[mid] > nums[l]: # means left half is sorted
                if target >= nums[l] and target <= nums[mid]: # in right half
                    r = mid
                else: # in left half
                    l = mid
        return -1


