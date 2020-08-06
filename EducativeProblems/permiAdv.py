import math


class Solution:
    def numTrees(self, n: int) -> int:
        return math.comb(2*n, n) // (n+1)

    def numTreeDP(self, n: int) -> int:
        output = [0 for _ in range(n+1)]
        print(output)
        output[0]= 1
        output[1]= 1
        for i in range(2,n+1):
            for j in range(i):
                output[i] = output[i] + (output[j] * output[i-j-1])
        return output[n]


obj = Solution()
print(obj.numTrees(3))
print(obj.numTreeDP(3))




def generatePerm(number:int)->list:
    if number==0:
        return []
    output = []
    subsets=[]
    output.append([])
    for n in range(1,number+1):
        currentLength = len(output)
        for j in range(currentLength):
            currentList = list(output[j])
            for k in range(len(currentList)+1):
                newList = list(currentList)
                newList.insert(k,n)
                if len(newList) == number:
                    subsets.append(newList)
                output.append(newList)
    return subsets

# print(len(sorted(generatePerm(3))))




