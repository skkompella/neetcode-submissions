class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # base case
        if n == 0: 
            return ['']
        out = set()
        if n == 1:
            out.add('()')
        else:
            # tmp1 = self.generateParenthesis(n-1)

            # proc1 = ['(' + t + ')' for t in tmp1]
            # proc2 = ['()' + t for t in tmp1]
            # proc3 = [t + '()' for t in tmp1]
            # for i in proc1:
            #     out.add(i)
            # for i in proc2:
            #     out.add(i)
            # for i in proc3:
            #     out.add(i)
            # # out = proc1+proc2

            for i in range(0, n):
                tmp1 = self.generateParenthesis(i)
                tmp2 = self.generateParenthesis(n-i-1)
                for j in tmp1:
                    for k in tmp2:
                        jon = '(' + k + ')' + j
                        out.add(jon)
        return list(out)