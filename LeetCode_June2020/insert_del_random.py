# from random import choice
from collections import Counter
import random

class RandomizedSet:

    def __init__(self):
        self.my_set = set()


    def insert(self, val: int) -> bool:
        if val in self.my_set:
            return False
        self.my_set.add(val)
        return True


    def remove(self, val: int) -> bool:
        if val in self.my_set:
            self.my_set.remove(val)
            return True
        return False


    def getRandom(self) -> int:
        if not self.my_set or len(self.my_set)==0:
            return -1
        return random.sample(self.my_set,1)



obj = RandomizedSet()
for i in range(1,5):
    obj.insert(i)

output = []
total = 1000000
for i in range(total):
    # print(obj.getRandom()[0])
    output.append(obj.getRandom()[0])

count = Counter(output)
for k,v in count.items():
    print(f'{k} : {(v/total)*100}')


# param_1 = obj.insert(10)
