def sum_rec(current_sum,idx,num):
    halfVal = sum(num)/2
    if idx >= len(num):
        return False
    elif current_sum + num[idx] == halfVal:
        return True
    elif current_sum + num[idx] > halfVal:
        return sum_rec(current_sum,idx+1,num)
    else:
        return sum_rec(current_sum + num[idx] , idx+1,num) or sum_rec(current_sum , idx+1,num)

def can_partition(num):
    return sum_rec(0,0,num)

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()