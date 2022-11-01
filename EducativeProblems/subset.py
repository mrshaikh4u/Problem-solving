from collections import deque
def find_subsets(nums):
    subsets = []
    if not nums or len(nums) ==0:
        return subsets
    subsets.append([])
    for i in nums:
        currentLength = len(subsets)
        for j in range(currentLength):
            currentList = list(subsets[j])
            currentList.append(i)
            subsets.append(currentList)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()