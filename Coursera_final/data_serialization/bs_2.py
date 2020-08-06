def count_rotations(arr):
    cnt = 0
    if not arr or len(arr) == 0:
        return -1
    found = False
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            found = True
            break
        cnt+=1
    if found:
        return cnt+1
    return 0


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


main()
