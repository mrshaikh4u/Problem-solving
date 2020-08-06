from collections import defaultdict
from collections import Counter
from datetime import datetime
def isPali(input:str)->bool:
    if not input or len(input)==0:
        return False
    input = input.lower()
    cnt = 0
    freq_cntr = defaultdict
    cntr = Counter(input)
    for vals in cntr.values():
        if vals%2 != 0:
            cnt+=1
    return not cnt>1

def checkPali(input:str)->bool:
    input = input.lower()
    return input[::] == input[::-1]

input = ["Anna",
 "Civic",
 "Kayak",
 "Level",
 "Madam",
 "Mom",
 "Noon",
 "Racecar",
 "Radar"]
strt =datetime.now()
for i in input:
    print(f"{i} : ",isPali(i))
end = datetime.now()
print("time for func : " , end-strt)
print("---------")

start = datetime.now()
for i in input:
    print(f"{i} : ",checkPali(i))
endt = datetime.now()
print("time for simple : ",endt-start)