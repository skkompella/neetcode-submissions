class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = [[]]
        nums = sorted(nums)
        l = len(nums)-1
        old_num_len = 0
        for i in range(len(nums)-1, -1, -1):
            if i != l and nums[i+1] == nums[i]:
                    # second half copy
                    tmp = []
                    # print(old_num_len, len(out))
                    for idx in range(old_num_len, len(out)):
                        tmp.append(out[idx]+[nums[i]])
                    # print(i)
                    old_num_len = len(out)
                    out = out + tmp
            else:
                old_num_len = len(out)
                tmp = []
                for li in out:
                    tmp.append(li+[nums[i]])
                # print(i)
                out = out + tmp
        return out