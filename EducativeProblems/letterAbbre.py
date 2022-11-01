from collections import deque
def perm(input:str)->list:
    if not input or len(input)==0:
        return []
    output = [[]]
    for ch in input:
        length = len(output)
        for i in range(length):
            current_set = list(output[i])
            current_set.append(ch)
            output.append(''.join(str(i) for i in current_set))
    return output

print(perm("BAT"))

