class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [((x1)**2 + (y1)**2, [x1, y1]) for x1, y1 in points]
        heapq.heapify(points)
        res = []
        for i in range(k):
            res.append(heapq.heappop(points)[1])
        return res