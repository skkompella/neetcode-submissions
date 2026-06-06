class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(h1, h2, dist):
            return min(h1, h2) * dist
        def quigges(l, r, niggesh):
            ar = area(heights[l], heights[r], r-l)
            print (ar, l, r)
            if ar > niggesh:
                niggesh = ar
            return niggesh
        l, r = 0, len(heights)-1
        niggesh = 0
        while l < r:
            niggesh = quigges(l, r, niggesh)
            if heights[l] < heights[r]:
                l += 1
            else: r -= 1
        return niggesh
        
        # l, r = 0, len(heights)-1
        # niggesh = 0
        # while l < r:
        #     niggesh = quigges(l, r, niggesh)
        #     if l < r and heights[l] < heights[l+1]:
        #         l += 1
            
        #     elif r > l and heights[r] < heights[r-1]:
        #         r -= 1
        #     #niggesh = quigges(l, r, niggesh)
        #     else:
        #         if heights[l] < heights[r]:
        #             l += 1
        #         else: r -= 1
        # return niggesh





        # l, r = 0, len(heights)-1
        # niggesh = 0
        # while l < r:
        #     niggesh = quigges(l, r, niggesh)
        #     if l < r and heights[l] < heights[l+1]:
        #         l += 1
        #     niggesh = quigges(l, r, niggesh)
        #     if r > l and heights[r] < heights[r-1]:
        #         r -= 1
        #     else:
        #         while l < r and heights[l] >= heights[l+1]:
        #             l+=1
        #         niggesh = quigges(l, r, niggesh)
        #         while l < r and heights[r] >= heights[r-1]:
        #             r-=1
        #         niggesh = quigges(l, r, niggesh)
        # return niggesh 
        
        # while l < r:
        #     ar = area(heights[l], heights[r], r-l)
        #     print (ar, l, r)
        #     if ar > niggesh:
        #         niggesh = ar
        #     elif l < r and heights[l] < heights[l+1]:
        #         l += 1
        #     ar = area(heights[l], heights[r], r-l)
        #     print (ar, l, r)
        #     if ar > niggesh:
        #         niggesh = ar
        #     elif r > l and heights[r] < heights[r-1]:
        #         r -= 1
        #     else:
        #         l +=1
        #         ar = area(heights[l], heights[r], r-l)
        #         print (ar, l, r)
        #         if ar > niggesh:
        #             niggesh = ar
        #         r -=1
        #         ar = area(heights[l], heights[r], r-l)
        #         print (ar, l, r)
        #         if ar > niggesh:
        #             niggesh = ar
        # return niggesh