class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        i=0
        while i < (len(temperatures)):
            j = i
            while j < len(temperatures) and (len(stack)==0 or temperatures[j]<=stack[0]):
                stack.append(temperatures[j])
                j+=1
                # print(stack)
            if j < len(temperatures) and temperatures[j]>stack[0]:
                result.append(len(stack))
                stack.clear()
                i+=1
                j=0
                # print(stack)
            # print(result)
            # if j >=len(temperatures):
            else:
                result.append(0)
                stack.clear()
                i+=1
                j=0
                # print(stack)
        return result