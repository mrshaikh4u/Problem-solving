def weighted_mean(numbers:list,weights:list):
    sum = 0.0
    weight_sum = 0.0
    for i in range(len(numbers)):
        sum+=(numbers[i]*weights[i])
        weight_sum+=weights[i]
    print('{:.1f}'.format(sum/weight_sum))

n = int(input())
numbers = list(map(int,input().split()))
weights = list(map(int,input().split()))
weighted_mean(numbers,weights)
