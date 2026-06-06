class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1
        while (L < R):
            while (L < R and not self.alphaNum(s[L])):#(s[L].isalpha() or s[L].isnumeric())):
                L = L + 1
            while (R > L and not self.alphaNum(s[R])):#(s[R].isalpha() or s[R].isnumeric())):
                R = R - 1
            print(s[L], s[R])
            if (s[L].lower() != s[R].lower()):
                return False
                # print(s[L], s[R])
             
            L = L + 1
            R = R - 1
        return True

        
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         L, R = 0, len(s) - 1

#         while L < R:
#             while L < R and not self.alphaNum(s[L]):
#                 L += 1
#             while R > l and not self.alphaNum(s[R]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l, r = l + 1, r - 1
#         return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
     
        
        
        
        
        
        
        
        
        # s = s.lower()
        # s = list(s)
        # lingesh = []
        # for x in s:
        #     if (x.isalpha() or x.isdigit()):
        #         print(x)
        #         lingesh.append(x)
        # print(lingesh)
        # s = lingesh
        # jiggesh = s[::-1]
        # # if len(s)%2 == 0:
        # print(s[0:(math.floor(len(s)/2))])
        # print(jiggesh[0:(math.floor(len(s)/2))])
        # if s[0:(math.floor(len(s)/2))] == jiggesh[0:(math.floor(len(s)/2))]:
        #     return True
        # else:
        #     return False
            