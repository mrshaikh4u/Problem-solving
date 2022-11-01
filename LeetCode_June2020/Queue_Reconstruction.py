from typing import List
from itertools import repeat

class Solution:

    def reconstructQueue_simpler(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return people
        people.sort(reverse=True)
        people.sort(key= lambda x : (-x[0],x[1]))
        print(people)
        output = []
        for i in people:
            output.insert(i[1],i)
        return output

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return people
        people.sort()
        # print('sorted: ', people)
        output = list(repeat(-1,len(people)))
        for i in people:
            cnt = i[1]
            idx = 0
            while idx < (len(output)-1) and cnt >0:
                if output[idx] == -1 or output[idx][0] >= i[0]:
                    cnt-=1
                idx+=1
            while idx < (len(output)-1) and output[idx]!=-1:
                idx+=1
            output[idx] = i
        return output
#[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
obj = Solution()
input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# print(obj.reconstructQueue(input))
print(obj.reconstructQueue_simpler(input))


