class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-i for i in nums]
        self.k = k
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        tmp = []
        for i in range(self.k):
            jon = heapq.heappop(self.heap)
            tmp.append(jon)
        res = -tmp[-1]
        for i in tmp:
            heapq.heappush(self.heap, i)
        print(self.heap, tmp)
        return res
