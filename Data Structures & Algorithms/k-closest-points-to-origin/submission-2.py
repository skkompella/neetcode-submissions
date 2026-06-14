class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(math.sqrt((x1)**2 + (y1)**2), [x1, y1]) for x1, y1 in points]
        heapq.heapify(points)
        res = []
        for i in range(k):
            tmp = heapq.heappop(points)
            res.append(tmp[1])
        return res