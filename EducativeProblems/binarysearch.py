def search_next_letter(letters, key):
    if not letters or len(letters)==0:
        return key
    if key < letters[0] or key > letters[len(letters)-1]:
        return letters[0]
    start = 0
    end = len(letters)-1
    while start<=end:
        mid = start+(end-start)//2
        if letters[mid] == key:
            if mid + 1 < len(letters):
                return letters[mid+1]
            else:
                return letters[0]
        if letters[mid] < key:
            start = mid+1
        else:
            end = mid-1
    return letters[start%len(letters)]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))


main()