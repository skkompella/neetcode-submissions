class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        def isAnagram(str1, str2):
            if sorted(str1) == sorted(str2):
                return True
            else: return False

        # for x in range(len(strs)):
        #     for y in range(len(strs)):
        #         if (x != y) & (isAnagram(strs[x], strs[y])):
        #             anagrams.append([strs[x], strs[y]])
        # return anagrams
        for x in strs:
            if str(sorted(x)) not in anagrams:
                anagrams[str(sorted(x))] = [x]
            elif str(sorted(x)) in anagrams:
                anagrams[str(sorted(x))].append(x)
        return anagrams.values()