testcases= int(input())
for t in range(testcases):
    input_str = input()
    cnt = 0
    i=0
    while i in range(len(input_str)-1):
        if input_str[i]!=input_str[i+1]:
            cnt+=1
            i+=1
        i+=1
    print(cnt)



