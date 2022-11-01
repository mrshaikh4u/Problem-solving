def find_letter_case_string_permutations(string):
    permutations = []
    if not string or len(string)==0:
        return permutations
    permutations.append(string)
    for k in range(len(string)):
        if string[k].isnumeric():
            continue
        currentLength = len(permutations)
        for i in range(currentLength):
            set = list(permutations[i])
            if set[k].islower():
                set[k] = set[k].upper()
            else:
                set[k] = set[k].lowe()
            permutations.append("".join(str(i) for i in set))
    return permutations


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()