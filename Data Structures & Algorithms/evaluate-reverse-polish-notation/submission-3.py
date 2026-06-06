class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        moddaNiggesh = []
        for x in tokens:
            if (x.isdigit() or x[1:].isdigit()):
                moddaNiggesh.append(x)
            else:
                if len(moddaNiggesh) >= 2:  #and (x == '+' or x == '-' or x == '/' or x == '*')
                    if x == '+':
                        z = int(moddaNiggesh[-2]) + int(moddaNiggesh[-1])
                        moddaNiggesh.pop()
                        moddaNiggesh.pop()
                        moddaNiggesh.append(z)
                    if x == '*':
                        z = int(moddaNiggesh[-2]) * int(moddaNiggesh[-1])
                        moddaNiggesh.pop()
                        moddaNiggesh.pop()
                        moddaNiggesh.append(z)
                    if x == '/':
                        z = int(int(moddaNiggesh[-2]) / int(moddaNiggesh[-1]))
                        moddaNiggesh.pop()
                        moddaNiggesh.pop()
                        moddaNiggesh.append(z)
                    if x == '-':
                        z = int(moddaNiggesh[-2]) - int(moddaNiggesh[-1])
                        moddaNiggesh.pop()
                        moddaNiggesh.pop()
                        moddaNiggesh.append(z)
            print(moddaNiggesh)
        return int(moddaNiggesh[0])
                