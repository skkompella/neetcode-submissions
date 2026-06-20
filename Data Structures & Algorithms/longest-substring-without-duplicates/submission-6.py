class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, = 0, 0
        max_cnt = 0
        cnt = 0
        sub = set()
        while r < len(s):
            if s[r] not in sub:
                sub.add(s[r])
                cnt += 1
                r += 1
            else: # s[r] is in the substring
                max_cnt = max(max_cnt, cnt)
                cnt = 0
                sub = set()
                l += 1
                r = l
        max_cnt = max(max_cnt, cnt)
        return max_cnt