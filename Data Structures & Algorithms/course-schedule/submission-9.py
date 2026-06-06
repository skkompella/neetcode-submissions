class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        graph = [[] for x in range(numCourses)] # course : [prereqs]
        in_degree = [0] * numCourses
        q = collections.deque()
        for x in prerequisites:
            graph[x[1]].append(x[0])
            in_degree[x[0]] += 1
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)
        visited = 0
        while len(q) != 0:
            course = q.popleft()
            # if course not in visited:
            #     visited.append(course)
            visited += 1
            for c in graph[course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    q.append(c)
        if visited == numCourses:
            return True
        return False