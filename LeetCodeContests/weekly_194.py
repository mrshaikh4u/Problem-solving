import re
from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        output = 0
        for i in range(n):
            output^=(start+2*i)
        return output

    def getFolderNames(self, names: List[str]) -> List[str]:
        # pattern = r'\(([1-9]*)\)$'
        cache = set()
        cntr = {}
        output = []
        for n in names:
            if n in cache:
                sp=1
                if n in cntr:
                    sp= cntr[n]
                while n+'('+str(sp)+')' in cache:
                    sp+=1
                cntr[n] = sp
                n = n+'('+str(sp)+')'
            cache.add(n)
            output.append(n)
        return output
    def avoidFlood(self, rains: List[int]) -> List[int]:
        output = [-1 for _ in rains]
        rain_set = set()
        zero_tracker = deque()
        for i in range(len(rains)):
            if rains[i] > 0:
                if rains[i] in rain_set:
                    if len(zero_tracker)<=0:
                        return []
                    output[zero_tracker.popleft()] = rains[i]
                    rain_set.remove(rains[i])
                else:
                    rain_set.add(rains[i])
            else:
                if len(rain_set)>0:
                    zero_tracker.append(i)
                else:
                    output[i] = 1
        for i in zero_tracker:
            output[i] = 1
        return output

    def getFolderNames_bk(self, names: List[str]) -> List[str]:
        pattern = r'\(([1-9]*)\)$'
        suff = 1
        suffMap = defaultdict(1)
        cache = set()
        output = []
        for n in names:
            changedSP = False
            if n in cache:
                result = re.search(pattern,n)
                if result is not None:
                    sp=1
                    while n+'('+str(sp)+')' in cache:
                        sp+=1
                    n = n+'('+str(sp)+')'
                else:
                    n= n+'('+str(suff)+')'
                    suff+=1
                    changedSP = True
            if not changedSP:
                result = re.search(pattern,n)
                if result is not None:
                    suff+=1
            cache.add(n)
            output.append(n)
        return output

obj = Solution()
# print(obj.getFolderNames(["pes","fifa","gta","pes(2019)"]))
# print(obj.getFolderNames(["pes(1)"]))
# print(obj.getFolderNames(["gta","gta(1)","gta","avalon"]))
# print(obj.getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]))
# print(obj.getFolderNames(["wano","wano","wano","wano"]))
# print(obj.getFolderNames(["t","l(1)(3)","o","i(3)(1)","j(1)","g","z","z","q(3)(2)","u(1)(3)","x","m","l(4)(2)","o","h","s","e","c","v"]))
# print(obj.getFolderNames(["kaido","kaido(1)","kaido","kaido(2)","kaido(1)(1)"]))
print(obj.avoidFlood([1,2,0,0,2,1]))
print(obj.avoidFlood([1,2,0,1,2]))
print(obj.avoidFlood([69,0,0,0,69]))
print(obj.avoidFlood([10,20,20]))
print(obj.avoidFlood([1,2,3,4]))
print(obj.avoidFlood([0,1,1]))
# obj.avoidFlood([1,2,3])