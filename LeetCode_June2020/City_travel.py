from typing import List
from operator import itemgetter


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        first_cost = [i for i,j in costs]
        arr_diff = [j-i for i,j in costs]
        arr_diff.sort()
        output  = sum(first_cost)
        i=0
        while i < len(arr_diff)//2:
            output+=arr_diff[i]
            i+=1
        return output

obj = Solution()
input_list = [[10,20],[30,200],[400,50],[30,20]]
print(input_list)
print(obj.twoCitySchedCost(input_list))


