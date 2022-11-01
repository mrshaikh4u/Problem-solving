import sys
from typing import List

deno = [10]
def findSum(sum):
    array = [sys.maxsize for _ in range(sum+1)]
    # print(array)
    array[0]=0
    for d in deno:
        for i in range(len(array)):
            if i+d < len(array) and array[i+d] > array[i]+1:
                array[i+d] = array[i]+1
    print(array[sum])

def findtotalSum(sum):
    a = [1] + [0]*sum
    for d in deno:
        for i in range(d,len(a)):
            a[i]+=a[i-d]
    print(a[sum])

def change(amount: int, coins: List[int]) -> int:
    s = [1]+[0]*amount
    for c in coins:
        for i in range(c,len(s)):
            s[i] += s[i-c]
    return s[-1]



print(change(5,[1,2,5]))
# findSum(11)
# findtotalSum(10)