class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s_map = {}
        for i in nums:
            if i not in s_map:
                s_map[i] = 0
            s_map[i]+=1
        for i in s_map.keys():
            if s_map[i] == 1:
                return i