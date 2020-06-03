from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        assert startTime,"start time is invalid"
        assert endTime , "end time is invalid"
        cnt=0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                cnt+=1
        return cnt
    def arrangeWords(self, text: str) -> str:
        word_list = text.split(' ')
        word_list[0] = word_list[0].lower()
        word_list.sort(key=len)
        word_list[0]= word_list[0].capitalize()
        return ' '.join(word_list)
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        output = []
        for i in range(len(favoriteCompanies)):
            isSubset = False
            for j in range(len(favoriteCompanies)):
                if i==j:
                    continue
                if set(favoriteCompanies[i]).issubset(set(favoriteCompanies[j])):
                    isSubset= True
            if not isSubset:
                output.append(i)
        return output

obj = Solution()
# print(obj.busyStudent([1,2,3],[3,2,7],4))
print(obj.arrangeWords("Leetcode is cool"))
