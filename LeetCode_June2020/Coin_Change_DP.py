from typing import List


class Solution:
    global deno

    def count(self,sum):
        cnt = 0
        for i in Solution.deno:
            mod = sum%i
            if mod in Solution.deno or mod == 0:
                if i==1:
                    cnt+=1
                else:
                    cnt+= sum // i
        return cnt

    def count_rec(self,sum):
        answer =0
        if sum in Solution.deno:
            answer = 1
        elif sum <= 0:
            answer = 0

        for d in Solution.deno:
            if d > sum:
                break
            else:
                current_ans = self.count_rec(sum-d) + 1
            answer*=current_ans
        # else:
        #     current_ans = 0
        #     answer = 1
        #     for d in Solution.deno:
        #         if d > sum:
        #             break
        #         else:
        #             current_ans = self.count_rec(sum-d) + 1
        #         answer*=current_ans
        #     # answer-=1
        return answer

# ans = 1
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        Solution.deno = coins
        return self.count_rec(amount)

obj = Solution()
print(obj.change(5,[1,2,5]))
