def BS(arr,key,start,end):
    mid = -1
    while start<=end:
        mid = start + ((end-start)//2)
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            end = mid-1
        else:
            start = mid+1
    return -1


def search_bitonic_array(arr, key):
    if not arr or len(arr) == 0:
        return -1
    start = 0
    end = len(arr)-1
    while start < end:
        mid = start + ((end-start)//2)
        if mid+1 < len(arr) and arr[mid] < arr[mid+1]:
            start = mid+1
        else:
            end = mid
    max_idx = start
    found_1 = BS(arr,key,0,max_idx)
    if found_1 != -1:
        return found_1
    else:
        return BS(arr,key,max_idx+1,len(arr)-1)

def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()