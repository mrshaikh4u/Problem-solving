from functools import lru_cache
def getmaxprofit(weight:list , profit:list , capacity:int)->list:
    output = []
    maxProfit = 0
    for i in range(len(weight)):
        currentCapacity = weight[i]
        currentProfit = profit[i]
        currentMax = 0
        currentPair = []
        currentPair.append(i)
        for j in range(i+1,len(weight)):
            if currentCapacity+weight[j] > capacity:
                continue
            currentCapacity+= weight[j]
            currentProfit+= profit[j]
            if currentMax < currentProfit:
                currentPair.append(j)
                currentMax = currentProfit
        if currentMax > maxProfit:
            output = list(currentPair)
    return output

profit = [1,6,10,16,12,15,19,20,18]
weight = [1,2,3,5,4,7,2,4,2]

@lru_cache(maxsize=10**6)
def knapSackRec(capacity:int , index:int)->int:
    print(f"{capacity} - {index}")
    if capacity <= 0 or index >= len(weight):
        return 0
    take = 0
    if weight[index] <= capacity:
        take = profit[index] + knapSackRec(capacity - weight[index] , index+1)
    notake = knapSackRec(capacity , index+1)
    return max(take,notake)

capacity = 25
print(knapSackRec(capacity,0))