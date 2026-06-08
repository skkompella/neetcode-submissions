class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        if len(nums) == 1:
            out.append([nums[0]])
        else:
            for i in range(len(nums)):
                tmp = nums.pop(i)
                jon = self.permute(nums)
                # print([tmp], jon)
                for j in range(len(jon)):
                    out.append([tmp]+jon[j])
                nums.insert(i, tmp)
        return out

