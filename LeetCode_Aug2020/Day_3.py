class MyHashSet:
    def __init__(self):
        self.data = [0 for _ in range(1000001)]

    def add(self, num: int):
        if self.data[num] != 1:
            self.data[num] = 1

    def contains(self, num: int) -> bool:
        return True if self.data[num] == 1 else False

    def remove(self, num: int):
        self.data[num] = 0

hashSet = MyHashSet();
hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))
print(hashSet.contains(3))
hashSet.add(2);
print(hashSet.contains(2))
hashSet.remove(2);
print(hashSet.contains(2))