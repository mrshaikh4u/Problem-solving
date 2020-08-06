from collections import deque
def find_permutations(nums):
    result = []
    if not nums or len(nums)==0:
        return result
    final_length = len(nums)
    queue = deque()
    queue.append([])
    for n in nums:
        currentLength = len(queue)
        for i in range(currentLength):
            currentList = list(queue.popleft())
            for j in range(len(currentList)+1):
                temp = list(currentList)
                temp.insert(j,n)
                if len(temp)==final_length:
                    result.append(temp)
                queue.append(temp)
    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()