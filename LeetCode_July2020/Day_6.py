from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits or len(digits) ==0:
            return digits
        output = list()
        c= 1
        for i in range(len(digits)-1,-1,-1):
            sum = digits[i] + c
            output.append(sum%10)
            c = sum//10
        if c > 0:
            output.append(c)
        output.reverse()
        print(output)

obj = Solution()
obj.plusOne([4,3,2,1])

