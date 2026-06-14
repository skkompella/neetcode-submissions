class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while (True):
            if len(heap) == 0:
                return 0
            elif len(heap) == 1:
                return -heap[0]
            one = -heapq.heappop(heap)
            two = -heapq.heappop(heap)
            if one != two:
                heapq.heappush(heap, -(one-two))

        