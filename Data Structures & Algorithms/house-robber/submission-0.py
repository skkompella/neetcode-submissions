class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        memo = {}
        def recurse(n):
            if l - n == 0:
                return 0
            if l - n == 1:
                return nums[n]
            if n not in memo:
                memo[n] = max(nums[n] + recurse(n+2), recurse(n+1))
            return memo[n]
        return recurse(0)
        