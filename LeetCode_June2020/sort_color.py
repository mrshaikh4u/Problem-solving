from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        ptr = len(nums)-1
        end = ptr
        print(nums)
        while start <= ptr:
            if nums[ptr] == 2:
                nums[ptr] , nums[end] = nums[end], nums[ptr]
                end-=1
                ptr-=1
            elif nums[ptr] == 0:
                nums[ptr] , nums[start] = nums[start]  ,nums[ptr]
                start+=1
            else:
                ptr-=1
        print(nums)

obj = Solution()
obj.sortColors([])