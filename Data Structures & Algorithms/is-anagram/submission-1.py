class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = []
        y = []
        for i in s:
            x.append(i)
        x = sorted(x)
        for i in t:
            y.append(i)
        y = sorted(y)
        if x != y:
            return False
        return True
        