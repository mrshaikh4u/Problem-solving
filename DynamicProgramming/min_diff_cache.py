input = [1, 2, 7, 1, 5]
count = 0
sum = 9

class result:
    def __init__(self):
        self.count=0
obj = result()
obj.count=0

def checkSum(idx:int , cs:int):
    if idx >= len(input):
        return 0
    if cs+input[idx] ==sum:
        obj.count+=1
    if cs+input[idx] < sum:
        checkSum(idx+1 , cs+input[idx])
    checkSum(idx+1,cs)

print(checkSum(0,0))
print(obj.count)

# @lru_cache(maxsize=10**6)
# def Rec(idx : int ,s1:int , s2:int)-> int:
#     if idx >= len(input):
#         return abs(s1-s2)
#     toS1Diff = Rec(idx+1 , s1+input[idx] ,s2)
#     toS2Diff = Rec(idx+1 , s1 , s2+input[idx])
#     return min(toS1Diff,toS2Diff)



# print(Rec(0,0,0))

