import sys
from functools import lru_cache
deno = [1,3,5]
@lru_cache(maxsize= 10**6)
def findRec(sum):
    print('called for : ',sum)
    answer = 0
    if sum <= 0:
        answer = 0
    else:
        current_min = sys.maxsize
        for d in deno:
            if d>sum:
                break
            current_min = min(findRec(sum-d)+1,current_min)
        answer = current_min
    return answer

def coin_itr(sum):
    sum = [0]+[sys.maxsize for _ in range(sum)]
    for d in deno:
        for i in range(d,len(sum)):
            if sum[i] > sum[i-d]+1:
                sum[i] = sum[i-d]+1
    return sum[-1]

print(findRec(11))
# print(coin_itr(11))