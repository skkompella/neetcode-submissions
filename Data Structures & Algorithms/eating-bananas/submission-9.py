import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # First calculate max pile size
        maxp = 0
        base = 1
        for p in piles:
            if p > maxp:
                maxp = p
        print(maxp)
        ans = maxp
        # piles eating time:
        def pilesTime(k):
            time = 0
            for p in piles:
                if p % k == 0:
                    time += p//k
                else:
                    time += (p//k + 1)
            return time


        # Second conduct binary search of K from 1 to maxp
        while (base <= maxp):
            # print(base)
            k = (base + maxp)//2
            t = pilesTime(k)
            if t > h:
                base = k+1
            elif t <= h:
                ans = k
                maxp = k-1
        return ans

