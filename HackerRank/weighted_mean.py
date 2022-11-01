import math
def weighted_mean(numbers:list,weights:list):
    summation = 0.0
    weight_summation = 0.0
    for i in range(len(numbers)):
        summation+=(numbers[i]*weights[i])
        weight_summation+=weights[i]
    print('{:.1f}'.format(summation/weight_summation))

def standard_deviation(numbers:list):
    summation = sum(numbers)
    mean = summation/len(numbers)
    summation=0.0
    for i in numbers:
        summation+=((i-mean)**2)
    summation/=len(numbers)
    print('{:.1f}'.format(math.sqrt(summation)))



n = int(input())
numbers = list(map(int,input().split()))
standard_deviation(numbers)
# weights = list(map(int,input().split()))
# weighted_mean(numbers,weights)
