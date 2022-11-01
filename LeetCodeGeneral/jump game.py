from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # filter out invalid arr
        if not arr:
            return False
        queue = deque()
        # adding root element as start
        queue.append(start)
        while queue:
            current_element = queue.popleft()
            # check for current element
            if arr[current_element]==0:
                return True
            # just to take backup as we are going to change this element to -1
            curr_val = arr[current_element]
            # setting it to -1 to eliminate it from iteration
            arr[current_element] = -1
            # left node as per problem description
            left = current_element - curr_val
            if left >=0 and arr[left] >=0:
                queue.append(left)
            # right not as per problem description
            right = current_element+curr_val
            if right < len(arr) and arr[right] >=0:
                queue.append(right)
        return False

obj = Solution()
print(obj.canReach([1,1,1,1,1,1,1,1,0],3))

