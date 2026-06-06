class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        width = len(grid)-1
        height = len(grid[0])-1
        
        q = collections.deque()
        for i in range(width+1):
            for j in range (height+1):
                if grid[i][j] == 0:
                    q.append([i, j])

        while len(q)!=0:
            jon = q.popleft()
            i, j = jon[0], jon[1]
            
            if (0 <= i+1 <= width and 0 <= j <= height):
                if grid[i+1][j] == inf:
                    grid[i+1][j] = 1 + grid[i][j]
                    q.append([i+1, j])
            if (0 <= i-1 <= width and 0 <= j <= height):
                if grid[i-1][j] == inf:
                    grid[i-1][j] = 1 + grid[i][j]
                    q.append([i-1, j])
            if (0 <= i <= width and 0 <= j+1 <= height):
                if grid[i][j+1] == inf:
                    grid[i][j+1] = 1 + grid[i][j]
                    q.append([i, j+1])
            if (0 <= i <= width and 0 <= j-1 <= height):
                if grid[i][j-1] == inf:
                    grid[i][j-1] = 1 + grid[i][j]
                    q.append([i, j-1])
