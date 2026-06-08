class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        if len(nums) == 1:
            out.append([nums[0]])
        else:
            for i in range(len(nums)):
                # print(i, nums)
                tmp = nums.pop(i)
                jon = self.permute(nums)
                # out.append([tmp] + jon)
                print([tmp], jon)
                # if len(jon) == 1:
                #     out.append([tmp] + jon)
                # else:
                for j in range(len(jon)):
                    out.append([tmp]+jon[j])
                # for j in range()
                # # for j in range(len(out)):
                # #     out[j].insert(0, tmp)
                # out = [[tmp] + row for row in out]
                nums.insert(i, tmp)
                # nums.append(tmp)
                # print(out)
        return out

