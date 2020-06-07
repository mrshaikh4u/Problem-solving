from typing import List
import heapq
from collections import deque


class BrowserHistory:

    def __init__(self, homepage: str):
        self.tab = deque()
        self.tab.append(homepage)
        self.top = len(self.tab)-1

    def visit(self, url: str) -> None:
        self.tab.append(url)
        self.top = len(self.tab)-1



    def back(self, steps: int) -> str:
        while self.top >= 0 and steps>0:
            self.top-=1
            steps-=1
        return self.tab[self.top]

    def forward(self, steps: int) -> str:
        if self.top>=len(self.tab)-1:
            return self.tab[self.top]
        while self.top < len(self.tab) and steps>0:
            self.top+=1
            steps-=1
        # self.tab = self.tab[:self.top+1]
        return self.tab[self.top]



# Your BrowserHistory object will be instantiated and called as such:
command = ["visit","visit","visit","back","back","forward","visit","forward","back","back"]
param = [["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

obj = BrowserHistory("leetcode.com")
for c in range(len(command)):
    if command[c]=="visit":
        obj.visit(param[c][0])
    elif command[c] == "back":
        print(obj.back(int(param[c][0])))
    elif command[c] == "forward":
        print(obj.forward(int(param[c][0])))



class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if not nums:
            return nums
        output = []
        j = 2*n//2
        i=0
        while i<(2*n)//2:
            output.append(nums[i])
            output.append(nums[j])
            i+=1
            j+=1
        return output
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        if not arr:
            return arr
        arr.sort()
        median = (len(arr)-1 )//2
        my_heap = []
        heapq.heapify(my_heap)
        for i in arr:
            diff = abs(arr[median]-i)
            heapq.heappush(my_heap,[diff,i])
        to_return = heapq.nlargest(k,my_heap)
        output = []
        for i in to_return:
            output.append(i[1])
        return output





# [2,1,4,3,5]
# queue = deque()
# queue.append(2)
# queue.append(1)
# queue.append(4)
# queue.append(3)
# queue.append(5)
# queue = queue.
# print(queue)


# top = len(queue)-1
# print('current : ',queue[top])
# # back
# # back
# top-=1
# top-=1
# print("back back : ",queue[top])
# # ]
# #
# # print(queue)
# # print(queue.popleft())
# # print(heapq.)
#
#
# # obj = Solution()
# # # obj.shuffle([1,2,3,4,4,3,2,1],4)
# # obj.getStrongest([1,1,3,5,5],2)
