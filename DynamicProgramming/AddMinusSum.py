
global a
global cnt
global sum
cnt = 0
a=[]
sum = 0


def findSumRec(currentSum : int , idx: int):
    global a
    global cnt
    global sum
    if idx>=len(a):
        return
    # if currentSum + a[idx] == sum:
    #     cnt+=1
    # elif currentSum - a[idx] == sum:
    #     cnt+=1
    if (currentSum + a[idx]) > sum:
        if a[idx] + findSumRec(currentSum , idx+1):
            cnt+=1
        if a[idx] + findSumRec(currentSum-a[idx] , idx+1):
            cnt+=1
    else:
        if a[idx] + findSumRec(currentSum , idx+1):
            cnt+=1
        if a[idx] + findSumRec(currentSum-a[idx] , idx+1):
            cnt+=1
        if a[idx] + findSumRec(currentSum+a[idx] , idx+1):
            cnt+=1

def find_target_subsets(num, s):
    global a
    global sum
    global cnt
    a = num
    sum = s
    cnt = 0
    findSumRec(0,0)
    return cnt

def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()