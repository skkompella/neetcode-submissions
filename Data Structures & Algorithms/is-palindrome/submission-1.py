class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        lingesh = []
        for x in s:
            if (x.isalpha() or x.isdigit()):
                print(x)
                lingesh.append(x)
        print(lingesh)
        s = lingesh
        jiggesh = s[::-1]
        # if len(s)%2 == 0:
        print(s[0:(math.floor(len(s)/2))])
        print(jiggesh[0:(math.floor(len(s)/2))])
        if s[0:(math.floor(len(s)/2))] == jiggesh[0:(math.floor(len(s)/2))]:
            return True
        else:
            return False
            