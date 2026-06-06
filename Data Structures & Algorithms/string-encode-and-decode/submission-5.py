class Solution:

    def encode(self, strs: List[str]) -> str:
        f = ''
        for x in strs:
            f += str(len(x))
            f += '_'
            f += x
        print(f)
        return f
    def decode(self, s: str) -> List[str]:
        moddaJiggesh = []
        # print(s)
        x = 0
        while x < len(s):
            i = x
            #j = x
            while (s[i] != '_'):
                i += 1
            print(x, i)
            num = int(s[x:i])
            x = i+1
            i = x + num
            moddaJiggesh.append(s[x:i])
            x = i
        return moddaJiggesh
            
            
            
            
            # try:
            #     while (s[i] != '_') & (x<len(s)):
            #         i +=1
            #     num = s[x:i]
            #     if (num.isdigit()):
            #         jiggesh = ''
            #         for j in range(int(num)):
            #             jiggesh+=(s[i+1+j])
            #             #print(jiggesh)
            #         print(jiggesh)
            #         moddaJiggesh.append(jiggesh)
            #         if(x == len(s)):
            #             print(five)
            # except Exception as e:
            #     print(moddaJiggesh)
            #     return moddaJiggesh

            # try:
            #     int(s[x])
            #     if ((x != (len(s)-1))):
            #         print(s[x])
            #         if  s[x+1] == '_':
            #             Jiggesh = ''
            #             for i in range(int(s[x])):
            #                 #print(s[x+2+i])
            #                 Jiggesh += (s[x+2+i])
            #             moddaJiggesh.append(Jiggesh)
            # except:
            #     #print(x)
            #     print('')
            # if x == '_':
            #     moddaJiggesh.append('')
            # else:
            #     moddaJiggesh[-1] += x
            # print (x)
            # try:
            #     z = int(x)
            #     moddaJiggesh.append('')
            # except Exception as e:
            #     moddaJiggesh[-1] += x
        