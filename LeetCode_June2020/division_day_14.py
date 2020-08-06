from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums or len(nums)==0:
            return nums
        nums.sort()
        mi = 0
        ml = 1
        length = [1 for _ in range(len(nums))]
        idx = [-1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j]==0:
                    if length[j] + 1 > ml:
                        ml = length[j]+1
                        mi = i
                        length[i] =  length[j]+1
                        idx[i] = j
                    else:
                        length[i] = max(length[i], length[j]+1)
                        idx[i] = max(idx[i],j)
        # print(idx)
        # print(mi)
        output = [-1 for _ in range(ml)]
        # output[ml-1] = nums[mi]
        ni = mi
        i=0
        while ni != -1:
            output[ml-1-i] = nums[ni]
            ni = idx[ni]
            i+=1
        return output

obj = Solution()
# print(obj.largestDivisibleSubset([1,3,4,9,27]))
# print(obj.largestDivisibleSubset([4,8,10,240]))
print(obj.largestDivisibleSubset([1,2,4,8]))