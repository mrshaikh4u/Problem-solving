from typing import List

# [-4, -1, -1, 0, 1, 2]
class Solution:
    def findData(self,nums:list , start : int , key:int , output)->bool:
        end = len(nums) - 1
        while start < end:
            diff = key - nums[start]
            if diff == nums[end]:
                output.append([nums[start],nums[end]])
                start+=1
                end-=1
                while start < end and nums[start] == nums[start-1]:
                    start+=1
                while start < end and nums[end] == nums[end+1]:
                    end-=1
            elif diff < nums[end]:
                end-=1
            else:
                start+=1
        if len(output) > 0:
            return True
        return False

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums)==0:
            return nums
        output = []
        nums.sort()
        print(nums)
        for i in range(0,len(nums)-2):
            if i>0 and nums[i] ==nums[i-1]:
                continue
            pair = []
            if self.findData(nums , i+1 , -nums[i],pair):
                for l in pair:
                    l.append(nums[i])
                    output.append(l)
        return output
obj = Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4]))
print(obj.threeSum([-3, 0, 1, 2, -1, 1, -2]))
print(obj.threeSum([-5, 2, -1, -2, 3]))
print(obj.threeSum([-2,0,0,2,2]))



