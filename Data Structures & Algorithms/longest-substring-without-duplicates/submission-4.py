class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        right = 0
        left = 0
        count = 0
        maxCount = 0
        sub = ''
        while (right < len(s)):
            print(sub)
            if s[right] not in sub:
                sub += s[right]
                count += 1
                right += 1
                if count > maxCount:
                    maxCount = count
            else:
                if count > maxCount:
                    maxCount = count
                count = 0
                left += 1
                right = left
                sub = ''
        return maxCount
            