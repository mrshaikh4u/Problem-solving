from typing import List
from random import choices
from collections import Counter
import os

os.wa

class Solution:

    def __init__(self, w: List[int]):
        self.weight = w
        total = sum(w)
        self.probability = [None] * len(w)
        for i in range(len(w)):
            self.probability[i]= w[i]/total


    def pickIndex(self) -> int:
        output = choices(range(len(w)),self.probability)
        return output[0]



w =[1,3]
obj = Solution(w)
output = []
total = 10000
for i in range(total):
    output.append(obj.pickIndex())
# print(output)
count = Counter(output)
for k,v in count.items():
    print(f'{k} : {(v/total)*100}')

