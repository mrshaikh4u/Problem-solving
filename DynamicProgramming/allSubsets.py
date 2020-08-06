from collections import deque

# [8 7 5 ]

def preparesubSets(input:list)->[]:
    output = []
    if not input or len(input) ==0:
        return output
    queue = deque()
    queue.append(set())
    while queue:
        currentLength = len(queue)
        for i in range(currentLength):
            temp = set(queue.popleft())
            for item in input:
                newList = set(temp)
                newList.add(item)
                output.append(newList)
                queue.append(newList)

    return output

print(preparesubSets([8,7,5]))