from typing import List
import sys
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = [0 for _ in range(len(prices))]
        output[-1] = prices[len(prices)-1]
        for i in range(len(prices)-2 , -1 , -1):
            if prices[i+1] <= prices[i]:
                output[i] = prices[i] - prices[i+1]
            else:
                if output[i+1] == prices[i+1]:
                    output[i] = prices[i]
                else:
                    found = False
                    for j in list(prices[i+1:]):
                        if j <= prices[i]:
                            output[i] = prices[i] - j
                            found = True
                            break
                    if not found:
                        output[i] = prices[i]
                    # output[i] = prices[i] - (prices[i+1] - output[i+1])
        return output
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        ws = 0
        sum = 0
        len1 = sys.maxsize
        len2 = sys.maxsize
        cnt = 0
        for we in range(len(arr)):
            sum+=arr[we]
            while sum > target and (we - ws +1) > 0:
                sum -= arr[ws]
                ws+=1
            if sum == target:
                cnt+=1
                if len1 > (we-ws+1):
                    if len2 > len1:
                        len2 = len1
                    len1 = (we-ws+1)
                elif len2 > (we-ws+1):
                    len2 = (we-ws+1)
                ws = we+1
                sum=0
        if cnt > 1:
            return len1+ len2
        return -1

obj = Solution()
# print(obj.finalPrices([5,4,10,2,6,1,1,1,9,1]))
print(obj.minSumOfLengths( [78,18,1,94,1,1,1,29,58,3,4,1,2,56,17,19,4,1,63,2,16,11,1,1,2,1,25,62,10,69,12,7,1,6,2,92,4,1,61,7,26,1,1,1,67,26,2,2,70,25,2,68,13,4,11,1,34,14,7,37,4,1,12,51,25,2,4,3,56,21,7,8,5,93,1,1,2,55,14,25,1,1,1,89,6,1,1,24,22,50,1,28,9,51,9,88,1,7,1,30,32,18,12,3,2,18,10,4,11,43,6,5,93,2,2,68,18,11,47,33,17,27,56,13,1,2,29,1,17,1,10,15,18,3,1,86,7,4,16,45,3,29,2,1,1,31,19,18,16,12,1,56,4,35,1,1,36,59,1,1,16,58,18,4,1,43,31,15,6,1,1,6,49,27,12,1,2,80,14,2,1,21,32,18,15,11,59,10,1,14,3,3,7,15,4,55,4,1,12,4,1,1,53,37,2,5,72,3,6,10,3,3,83,8,1,5],97))
# [1, 3, 2, 1, 7, 0, 0, 6, 9, 1]

# [78,18,1,94,1,1,1,29,58,3,4,1,2,56,17,19,4,1,63,2,16,11,1,1,2,1,25,62,10,69,12,7,1,6,2,92,4,1,61,7,26,1,1,1,67,26,2,2,70,25,2,68,13,4,11,1,34,14,7,37,4,1,12,51,25,2,4,3,56,21,7,8,5,93,1,1,2,55,14,25,1,1,1,89,6,1,1,24,22,50,1,28,9,51,9,88,1,7,1,30,32,18,12,3,2,18,10,4,11,43,6,5,93,2,2,68,18,11,47,33,17,27,56,13,1,2,29,1,17,1,10,15,18,3,1,86,7,4,16,45,3,29,2,1,1,31,19,18,16,12,1,56,4,35,1,1,36,59,1,1,16,58,18,4,1,43,31,15,6,1,1,6,49,27,12,1,2,80,14,2,1,21,32,18,15,11,59,10,1,14,3,3,7,15,4,55,4,1,12,4,1,1,53,37,2,5,72,3,6,10,3,3,83,8,1,5]
# 97