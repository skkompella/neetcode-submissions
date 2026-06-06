class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = []
        def dfs(li, num):
            if num == 0:
                out.append(li)
                return
            if num < 0:
                return
            for i in nums:
                jon = li[:]
                jon.append(i)
                jon.sort()
                if jon in out:
                    continue
                dfs(jon, num-i)
        dfs([], target)
        return out
