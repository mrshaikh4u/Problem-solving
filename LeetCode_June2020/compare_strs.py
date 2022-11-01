import re
def compare_strings(string1, string2):
    #Convert both strings to lowercase
    #and remove leading and trailing blanks
    # print('inside function')
    string1 = string1.lower().strip()
    string2 = string2.lower().strip()
    # print(string1)
    #Ignore punctuation
    punctuation = r"[.?!,-;:']"
    try:
        string1 = re.sub(punctuation,"", string1)
        string2 = re.sub(punctuation,"", string2)
    except Exception as e:
        print(e)

    #DEBUG CODE GOES HERE
    # print(f'string1 : {string1}')
    # print(f'string2 : {string2}')
    # print('string1 : {} string2 : {}'.format(string1,string2))

    return string1 == string2

# compare_strings("Have a Great Day!", "Have a great day?")
print(compare_strings("Have a Great Day!", "Have a great day?")) # True
print(compare_strings("It's raining again.", "its raining, again")) # True
print(compare_strings("Learn to count: 1, 2, 3.", "Learn to count: one, two, three.")) # False
print(compare_strings("They found some body.", "They found somebody.")) # False