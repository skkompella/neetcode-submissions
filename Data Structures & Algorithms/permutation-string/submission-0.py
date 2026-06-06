class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False

        s1_sorted = sorted(s1)

        map1 = {}
        map2 = {}
        for i in s1:
            if i in map1:
                map1[i] += 1
            else:
                map1[i] = 1
        
        for i in s2:
            if i in map2:
                map2[i] += 1
            else:
                map2[i] = 1
        
        i = 0
        while i < s2_len:
            # now i is at the start of the permutation
            left = i
            right = i + s1_len
            if s2[i] in map1:
                if s1_sorted == sorted(s2[left:right]):
                    return True
            i+=1
        return False
                
