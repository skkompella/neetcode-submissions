class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # base case
        if n == 0: 
            return ['']
        out = set()
        if n == 1:
            out.add('()')
        else:
            tmp1 = self.generateParenthesis(n-1)
            for seq in tmp1:
                for i in range(len(seq)):
                    seq_1 = seq[:i]
                    seq_2 = seq[i:]
                    out.add('('+seq_1+')'+seq_2)

            # for i in range(0, n):
            #     tmp1 = self.generateParenthesis(i)
            #     tmp2 = self.generateParenthesis(n-i-1)
            #     for j in tmp1:
            #         for k in tmp2:
            #             jon = '(' + k + ')' + j
            #             out.add(jon)
        return list(out)