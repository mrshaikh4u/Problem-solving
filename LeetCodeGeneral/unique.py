# input = [1,2,4,1,4,3,3]
# for i in range(1,len(input)):
#     input[0]^=input[i]
# print(input[0])

input = [1,1,1,2,3,3,3]
for i in range(1,len(input)):
    if input[0] ^ input[i] == 0:
        input[0]^=input[i]
        input[0]^=input[i]
    else:
        input[0]^=input[i]

print(input[0])


# a=10
# b=5
# a^=b
# a^=b
# a^=b
# print(a)
#
