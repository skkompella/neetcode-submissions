class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = -1
                    q.append([i, j])

        while len(q) != 0:
            jon = q.popleft()
            i, j = jon[0], jon[1]
            if (0 <= i+1 < len(grid) and 0 <= j < len(grid[0])):
                if grid[i+1][j] == 1:
                   grid[i+1][j] = grid[i][j] - 1
                   q.append([i+1, j])
            if (0 <= i-1 < len(grid) and 0 <= j < len(grid[0])):
                if grid[i-1][j] == 1:
                   grid[i-1][j] = grid[i][j] - 1 
                   q.append([i-1, j])
            if (0 <= i < len(grid) and 0 <= j+1 < len(grid[0])):
                if grid[i][j+1] == 1:
                   grid[i][j+1] = grid[i][j] - 1
                   q.append([i, j+1])
            if (0 <= i < len(grid) and 0 <= j-1 < len(grid[0])):
                if grid[i][j-1] == 1:
                   grid[i][j-1] = grid[i][j] - 1
                   q.append([i, j-1])
        
        min_val = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                if grid[i][j] < min_val:
                    min_val = grid[i][j]
        return abs(min_val+1)
                    