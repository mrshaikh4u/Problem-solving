def find_subsets(nums):
    subsets = []
    if not nums or len(nums) ==0:
        return subsets
    subsets.append([])
    prev = None
    for n in nums:
        currentLength = len(subsets)
        if prev == n:
            start = currentLength//2
        else:
            start = 0
        prev = n
        for i in range(start,currentLength):
            my_set = list(subsets[i])
            my_set.append(n)
            subsets.append(my_set)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()