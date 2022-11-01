from collections import deque
def find_permutations(nums):
    result = []
    queue = deque()
    final_length = len(nums)
    queue.append([])
    for n in nums:
        length = len(queue)
        for i in range(length):
            currentList = queue.popleft()
            for k in range(len(currentList)+1):
                new_list = list(currentList)
                new_list.insert(k,n)
                if len(new_list) == final_length:
                    result.append(new_list)
                queue.append(new_list)

    return result


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()