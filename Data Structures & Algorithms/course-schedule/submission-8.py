class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        graph = [[] for x in range(numCourses)] # course : [prereqs]
        print(len(graph))
        print(graph)
        # in_degree = [0] * numCourses
        in_degree = [0] * numCourses
        q = collections.deque()
        for x in prerequisites:
            graph[x[1]].append(x[0])
            in_degree[x[0]] += 1

            # if x[0] == x[1]:
            #     return False
            # if x[1] not in graph:
            #     graph[x[1]] = [x[0]]
            #     in_degree[x[1]] = 0
            # else:
            #     graph[x[1]].append(x[0])
            # if x[0] not in graph:
            #     graph[x[0]] = []
            #     in_degree[x[0]] = 1
            # else:
            #     in_degree[x[0]] += 1
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
        print(in_degree)
        print(graph)
        visited = []
        while len(q) != 0:
            course = q.popleft()
            if course not in visited:
                visited.append(course)
                for c in graph[course]:
                    in_degree[c] -= 1
                    if in_degree[c] == 0:
                        q.append(c)
        print(visited)
        if len(visited) == numCourses:
            return True
        return False