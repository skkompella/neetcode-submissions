class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = []
        def dfs(node, prev):
            if node in visited:
                return False
            visited.append(node)
            val = True
            for i in adj_list[node]:
                if i != prev:
                    val = val and dfs(i, node)
            return val

        
        lingesh = dfs(0, -1)
        print(visited)
        if len(visited) == n:
            return lingesh
        return False