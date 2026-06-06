class Solution:
    def reverseBits(self, n: int) -> int:
        jon = 0
        for i in range(32):
            jon = jon << 1
            if n%2 == 1:
                jon += 1
            # jon = jon << 1
            n = n >> 1
            print(jon, n)
        return jon
                