class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max = 0
        while (right < len(prices)):
            if max < prices[right] - prices[left]:
                max = prices[right] - prices[left]
            if prices[left] > prices[right]:
                left = right
                right = left + 1
            # elif prices[right+1] > prices[right]:
            else:
                right += 1


        return max