class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # points = [((x1)**2 + (y1)**2, [x1, y1]) for x1, y1 in points]
        # heapq.heapify(points)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(points)[1])
        # return res

        res = []
        for x1, y1 in points:
            dist = -((x1)**2 + (y1)**2)
            if len(res) < k:
                heapq.heappush(res, (dist, [x1, y1]))
            elif dist > res[0][0]:  # new point closer than farthest in heap
                heapq.heapreplace(res, (dist, [x1, y1]))
        return [point for _, point in res]