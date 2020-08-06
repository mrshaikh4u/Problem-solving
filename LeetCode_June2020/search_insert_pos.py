from typing import List


# Input: [1,3,5,6], 5
# Output: 2
# Example 2:
#
# Input: [1,3,5,6], 2
# Output: 1
# Example 3:
#
# Input: [1,3,5,6], 7
# Output: 4
# Example 4:
#
# Input: [1,3,5,6], 0
# Output: 0
# [1,3] = 2
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0 or target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        start = 0
        end = len(nums)-1
        mid = 0
        while start<=end:
            mid = start + ( (end - start )//2)
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return start

# [1,3,5,6], 5
obj = Solution()
print(obj.searchInsert([1,3],2)) # 1
print(obj.searchInsert([1,3,5,6],5)) # 2
print(obj.searchInsert([1,3,5,6],2)) # 1
print(obj.searchInsert([1,3,5,6],4)) # 4
print(obj.searchInsert([1,3,5,6],0)) # 0
print(obj.searchInsert([],2)) # 0
print(obj.searchInsert([1],1)) #0
