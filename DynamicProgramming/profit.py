from typing import List


# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0 :
            return 0
        s = prices[len(prices)-1]
        p = 0
        for i in range(len(prices)-2 , -1,-1):
            if prices[i] >= s:
                s = prices[i]
            elif s- prices[i] > p:
                    p = s-prices[i]
        return p


obj = Solution()
print(obj.maxProfit([7,6,4,3,1]))

