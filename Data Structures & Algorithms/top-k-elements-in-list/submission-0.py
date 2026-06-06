class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        jiggesh = {}
        lingesh = []
        for x in nums:
            if x not in jiggesh:
                jiggesh[x] = 0
            elif x in jiggesh:
                jiggesh[x] += 1
        for s in range(k):
            max_key = max(jiggesh, key=jiggesh.get)
            lingesh.append(max_key)
            del jiggesh[max_key]
        return lingesh