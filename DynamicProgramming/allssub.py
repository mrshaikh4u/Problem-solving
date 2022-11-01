from collections import deque
def allsub(input:str)->list:
    if not input or len(input)==0:
        return []
    output = []
    output.append("")
    for c in input:
        length = len(output)
        for i in range(length):
            set = list(output[i])
            set.append(c)
            output.append(''.join(str(j) for j in set))
    del output[0]
    return output

def allSubRec(output:list,input:str,idx:int)->None:
    length  = len(input)
    if idx >= length:
        return
    current_length = len(output)
    for i in range(current_length):
        current_list = list(output[i])
        current_list.append(input[idx])
        output.append(''.join(str(j) for j in current_list))
    if idx == length-1:
        return
    allSubRec(output , input , idx+1)

print(allsub("abc"))
input = "abc"
output = [""]
allSubRec(output,input,0)
del output[0]
print(output)
