from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return -1
        i=0
        while i in range(len(nums)):
            if nums[i] != i+1 and nums[i] != nums[nums[i]]:
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp
            else:
                i+=1

        for i in range(len(nums)):
            if nums[i]!=i+1:
                return nums[i]

    def findDuplicateNoExtraSpace(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return -1
        dup = -1
        for i in range(len(nums)):
            indx = abs(nums[i])
            if nums[indx] > 0:
                nums[indx] = -nums[indx]
            else:
                dup = abs(nums[i])
                break
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -nums[i]
        return dup


    def findDuplicateSort(self, nums: List[int]) -> int:
        if not nums or len(nums)==0:
            return -1
        sorted_data = sorted(nums)
        for i in range(len(sorted_data)-1):
            if sorted_data[i] == sorted_data[i+1]:
                return sorted_data[i]
        return -1


obj = Solution()
print(obj.findDuplicateNoExtraSpace([3,1,3,4,2]))
print(obj.findDuplicateNoExtraSpace([1,3,4,2,2]))
# print(obj.findDuplicate([1,1,4,2,3]))
# print(obj.findDuplicate([3,1,2,4,1]))
# print(obj.findDuplicate([3,1,3,4,2]))
