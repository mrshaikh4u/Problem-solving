def binarySearch(key:int,arr:list , start:int,end : int)->int:
    while start <= end:
        mid = start + ((end -start) //2)
        if arr[mid] == key:
            return mid
        if arr[mid] > key :
            end = mid - 1
        else:
            start = mid + 1
    return -1

def search_rotated_array(arr, key):
    if not arr or len(arr) == 0:
        return -1
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            break
    if i == len(arr)-1:
        return binarySearch(key,arr,0,len(arr)-1)
    else:
        first_return = binarySearch(key,arr,0,i)
        if first_return ==-1:
            return binarySearch(key,arr,i+1,len(arr)-1)
        return first_return
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()
