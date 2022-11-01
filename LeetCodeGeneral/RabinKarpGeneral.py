def getHash(string:str)->int:
    result = 0
    i=0
    for ch in reversed(string):
        result+= (ord(ch) - 96) * 10**i
        i+=1
    return result
def findPattern(input:str , pattern:str):
    pattern_hash = getHash(pattern)
    print(pattern_hash)
    pattern_length = len(pattern)
    ws = 0
    wh=0
    tocheck = []
    for we in range(len(input)):
        if we < pattern_length-1:
            continue
        if wh==0:
            wh = getHash(input[ws:we+1])
        else:
            old_val = (wh - ((ord(input[ws])-96) * (10**(pattern_length-1))))
            wh = (10 * old_val) + (ord(input[we])-96)
            ws+=1
        if wh == pattern_hash:
            tocheck.append(input[ws:we+1])
    print(tocheck)






findPattern("babab","")