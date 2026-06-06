class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        for i in nums:
            for j in out[:]:
                ron = j[:]
                ron.append(i)
                if ron not in out:
                    out.append(ron)

        return out