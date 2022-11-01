from typing import List


class Solution:

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     dp = [0 for i in range(len(cost) + 2)]
    #     dp[-1] = 0
    #     dp[-2] = 0
    #     for i in range(len(cost) -1, -1, -1):
    #         dp[i] = min(dp[i+1] + cost[i], dp[i+2] + cost[i])
    #     return min(dp[0], dp[1])


    def findCostRec(self,cost:List[int], length:int )->int:
        if length <= 1:
            answer = cost[length]
        else:
            oneback = self.findCostRec(cost,length-1) + cost[length]
            twoback = self.findCostRec(cost,length-2) + cost[length]
            answer = min(oneback,twoback)
            # answer = min(self.findCostRec(cost,length-1) + cost[length], self.findCostRec(cost,length-2)+cost[length])
        return answer

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [0 for _ in range(len(cost)+2)]
        for i in range(len(cost)-1 , -1,-1):
            cache[i] = min(cache[i+1] + cost[i] , cache[i+2]+cost[i])
        return min(cache[0],cache[1])


        # return self.findCostRec(cost,len(cost)-1)



#
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
obj = Solution()
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
# print(obj.minCostClimbingStairs([10, 15, 20]))