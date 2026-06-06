class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            jimgesh = numbers[l] + numbers[r]
            if jimgesh > target:
                r -= 1
            elif jimgesh < target:
                l += 1
            else:
                return[l+1, r+1]
        
        
        
        # l = 0
        # r = len(numbers)-1
        # while l < r:
        #     # if numbers[l] + numbers[r] == target:
        #     #     return [l+1, r+1]
        #     while (r > l+1) and (numbers[l] + numbers[r] > target):
        #         r -= 1
        #     if numbers[l] + numbers[r] == target:
        #         return [l+1, r+1]
        #     l += 1
        # return [l+1,r+1]