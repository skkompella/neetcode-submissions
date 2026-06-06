class Solution:
    def isValid(self, s: str) -> bool:
        stacc = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                stacc.append(x)

            elif x == ')' and len(stacc)>0 and stacc[-1] == '(':
                del stacc[-1]
            elif x == ']' and len(stacc)>0 and stacc[-1] == '[':
                del stacc[-1]
            elif x == '}' and len(stacc)>0 and stacc[-1] == '{':
                del stacc[-1]
            else:
                stacc.append(x)
        if len(stacc) == 0:
            return True
        return False