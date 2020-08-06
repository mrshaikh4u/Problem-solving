import math
import sys


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]

def findEnd(reader:ArrayReader,key):
    end = 0
    while reader.get(end) != sys.maxsize and key > reader.get(end):
        end*=2
    return end

def search_in_infinite_array(reader, key):
    # TODO: Write your code here
    start = 0
    end = findEnd(reader , key)
    mid = -1
    while start<=end:
        mid = start + (end-start)//2
        current_data = reader.get(mid)
        if current_data == key:
            return mid
        if current_data > key:
            end = mid-1
        else:
            start = mid+1
    return mid

def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 16))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))


main()






