def findRec(idx:int , currentSum : int , num:list,totalsum:int)->bool:
    if idx >= len(num):
        return False
    elif currentSum+num[idx] == totalsum:
        return True
    elif currentSum+num[idx] > totalsum:
        return findRec(idx+1 , currentSum , num , totalsum)
    else:
        return findRec(idx+1 ,currentSum+num[idx] , num, totalsum) or findRec(idx+1 , currentSum , num,totalsum)

# input = [1,2,7,1,5]
print("Can partition: " + str(findRec(0,0,[1, 2, 3, 7], 6)))
print("Can partition: " + str(findRec(0,0,[1, 2, 7, 1, 5], 10)))
print("Can partition: " + str(findRec(0,0,[1, 3, 4, 8], 6)))
