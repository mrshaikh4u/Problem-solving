import sys
def search_min_diff_element(arr, key):
    if not arr or len(arr) == 0 :
        return -1
    prev = sys.maxsize
    pi=-1
    start= 0
    end = len(arr)-1
    diff = sys.maxsize
    while start <= end:
        mid = start + end-start // 2
        diff = key - arr[mid]
        if abs(diff) > abs(prev):
            return arr[pi]
        prev = diff
        pi = mid
        if diff < 0:
            end = mid-1
        else:
            start = mid+1
    return arr[pi]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
