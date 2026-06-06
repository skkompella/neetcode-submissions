class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        jiggesh = []
        for i, x in enumerate(nums):
            if i > 0 and nums[i-1] == x:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                print(jiggesh)
                moddaJiggesh = x + nums[l] + nums[r]
                if moddaJiggesh < 0:
                    l += 1
                elif moddaJiggesh > 0:
                    r -= 1
                elif moddaJiggesh == 0:
                    jiggesh.append([x, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                
        return jiggesh
        
        
        # print(nums)
        # nums.sort()
        # #print (nums)
        # jiggesh = []
        # x = 0
        # def twosum(target, dingesh):
        #     l = 0
        #     r = len(dingesh)-1
        #     while l < r:
        #         cursum = dingesh[l] + dingesh[r]
        #         if cursum > target:
        #             r -= 1
        #         elif cursum < target:
        #             l += 1
        #     jiggesh.append([target, l, r].sorted())

        # while x < len(nums):
        #     lingesh = nums
        #     del lingesh[x]
        #     twosum(nums[x], lingesh)
        #     while nums[x] == nums[x+1]:
        #         x += 1
        # return jiggesh.unique()