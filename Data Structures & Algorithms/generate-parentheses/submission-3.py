class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # base case
        memo={}
        def helper(n):
            if n == 0: 
                return ['']
            out = set()
            if n == 1:
                out.add('()')
            else:
                # tmp1 = self.generateParenthesis(n-1)
                # for seq in tmp1:
                #     for i in range(len(seq)):
                #         seq_1 = seq[:i]
                #         seq_2 = seq[i:]
                #         out.add('('+seq_1+')'+seq_2)

                for i in range(0, n):
                    if i not in memo:
                        memo[i] = helper(i)
                    if n-i-1 not in memo:
                        memo[n-i-1] = helper(n-i-1)
                    tmp1 = memo[i]
                    tmp2 = memo[n-i-1]
                    for j in tmp1:
                        for k in tmp2:
                            jon = '(' + j + ')' + k
                            out.add(jon)
            return list(out)
        return helper(n)