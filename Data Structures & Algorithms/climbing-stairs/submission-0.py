class Solution:
    # cnt = 0
    def recurse(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.recurse(n-1) + self.recurse(n-2)      
    def climbStairs(self, n: int) -> int:
        # self.cnt = 0
        return self.recurse(n)
        # return self.cnt