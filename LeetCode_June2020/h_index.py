from typing import List


class Solution:


    def hIndex(self, citations: List[int]) -> int:
        if not citations or len(citations)==0:
            return 0
        start = 0
        length = len(citations)
        end = length-1
        mid = start
        while start <= end:
            mid = start + (end-start)//2
            if citations[mid] == length - mid:
                return citations[mid]
            if citations[mid] < length -mid:
                start = mid +1
            else:
                end = mid-1
        return length - start

    # def hIndex(self, citations: List[int]) -> int:
    #     if not citations or len(citations)==0:
    #         return 0
    #     start = 0
    #     end = len(citations)-1
    #     mid = start + (end - start)//2
    #     prev = -1
    #     while mid<len(citations) and len(citations) - mid >= citations[mid]:
    #         prev = mid
    #         start = mid
    #         mid = start + (end-start)//2
    #         if mid == prev:
    #             mid+=1
    #     return len(citations) - prev

    def hIndex_2(self,citations):
        h = 0
        for i in reversed(range(len(citations))):
            if h>=citations[i]: return h
            else: h+=1
        return h

obj = Solution()
print(obj.hIndex([0,1,3,5,6]))
# print(obj.hIndex_2([0,1,3,5,6]))
print(obj.hIndex([1,1,2,2,3,5]))
# print(obj.hIndex_2([1,1,2,2,3,5]))
print(obj.hIndex([0,1,1,1,1,1,2]))
# print(obj.hIndex_2([0,1,1,1,1,1,2]))
print(obj.hIndex([1,1,1]))
# print(obj.hIndex_2([1,1,1]))
print(obj.hIndex([1,2,3]))
# print(obj.hIndex_2([1,2,3]))
print(obj.hIndex([0,0]))
# print(obj.hIndex_2([0,0]))
print(obj.hIndex([0,0,0]))
# print(obj.hIndex_2([0,0,0]))




