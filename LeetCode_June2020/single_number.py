from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return -1
        if len(nums)==1:
            return nums[0]
        nums.sort()
        i=0
        while i < len(nums):
            if i+2 >= len(nums):
                return nums[i]
            if nums[i] != nums[i+1] or nums[i] != nums[i+2]:
                return nums[i]
            i+=3

obj = Solution()
# input = [2,2,2,3]
# input = [0,1,0,1,0,1,99]
input = [2,3,3,3,4,4,4]
print(obj.singleNumber(input))