import collections

def calculate_mean_median_mode(n:int,numbers:list):
    numbers.sort()
    sum=0.0
    mode_cnt = 0
    mode_val = None
    counter = collections.defaultdict(int)
    for i in numbers:
        sum+=i
        current_cnt = counter.get(i,0)
        current_cnt+=1
        counter.update({i:current_cnt})
        if current_cnt < mode_cnt:
            continue
        elif current_cnt == mode_cnt:
            mode_val = min(i,mode_val)
        else:
            mode_val = i
        mode_cnt = current_cnt
    mean = sum/len(numbers)
    length = len(numbers)
    if length%2==0:
        median = (numbers[(length//2)-1] + numbers[(length//2)] ) / 2
    else:
        median = numbers[length//2]
    print('{:.1f}'.format(mean))
    print('{:.1f}'.format(median))
    print(mode_val)


n=int(input())
numbers = list(map(int, input().split()))
calculate_mean_median_mode(n,numbers)