class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_len = len(word)-1
        board_len = len(board)
        board_len_0 = len(board[0])
        def recurse(word_idx, i, j):
            if word[word_idx] != board[i][j]:
                return False
            if word_idx==word_len and word[word_idx] == board[i][j]:
                return True
            
            tmp = board[i][j]
            board[i][j] = '#'
            # res1, res2, res3, res4 = False, False, False, False
            # if (i+1 < board_len):
            #     res1 = recurse(word_idx+1, i+1, j)
            # if (j+1 < board_len_0):
            #     res2 = recurse(word_idx+1, i, j+1)
            # if (i-1 >= 0):
            #     res3 = recurse(word_idx+1, i-1, j)
            # if (j-1 >= 0):
            #     res4 = recurse(word_idx+1, i, j-1)
            # res = res1 or res2 or res3 or res4
            # board[i][j] = tmp
            # return res
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < board_len and 0 <= nj < board_len_0:
                    if recurse(word_idx+1, ni, nj):
                        board[i][j] = tmp  # restore before early return
                        return True
            board[i][j] = tmp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if recurse(0, i, j) == True:
                    return True
        return False